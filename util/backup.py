#!/usr/bin/env python3

import docker
import os
import datetime

BACKUP_LABEL = 'backup_target'
BACKUP_CMD = '/usr/bin/mysqldump -u {} --password={} {}'

# Must have these environment variables (same environment variables for docker-compose)
REQUIRED_ENV = [
    'DB_DATABASE',
    'DB_USERNAME',
    'DB_PASSWORD',
    'BACKUP_PATH',
    'BACKUP_RETENTION'
]

def get_container_backupdir(name):
    return '{}/{}'.format(os.environ['BACKUP_PATH'], name)


def delete_oldest(directory):
    retcode = os.system('rm {}/$(ls -t {}/ | tail -1)'.format(directory, directory))
    assert retcode == 0, 'Bad exit code while trying to remove old dumps: {}'.format(retcode)


def check_retention(container_name):
    curr_backups = len([name for name in os.listdir(get_container_backupdir(container_name))])
    if curr_backups > int(os.environ['BACKUP_RETENTION']):
        for idx in range(0, curr_backups - int(os.environ['BACKUP_RETENTION'])):
            delete_oldest(get_container_backupdir(container_name))


def do_backup(db_container):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
    fname = '{}_{}.sql'.format(db_container.name, timestamp)

    if not os.path.exists(get_container_backupdir(db_container.name)):
        os.makedirs(get_container_backupdir(db_container.name))

    backup_path = '{}/{}'.format(get_container_backupdir(db_container.name), fname)

    cmd = BACKUP_CMD.format(
        os.environ['DB_USERNAME'],
        os.environ['DB_PASSWORD'],
        os.environ['DB_DATABASE']
    )

    exit_code, res = db_container.exec_run(cmd, stderr=False)
    assert exit_code == 0, 'Bad exit code while trying to dump db: {}'.format(exit_code)

    print('Saving backup to {}'.format(backup_path))
    with open(backup_path, 'wb') as f:
        f.write(res)

    

def main():
    client = docker.from_env()
    for container in client.containers.list():
        if BACKUP_LABEL in container.labels:
            print('Backing up container: {}'.format(container.name))
            do_backup(container)
            check_retention(container.name)

    

if __name__ == '__main__':
    for var in REQUIRED_ENV:
        assert var in os.environ, 'Missing required enviornment variable: {}'.format(var)

    main()