# Volume Backups

This is just a temporary document on how to backup and restore docker volumes before I formalize it in a script.

## Backup

```bash
docker run -it --rm -v fortitudoincinfra_proxy:/volume -v /tmp/volumes:/backup alpine tar -cjf /backup/fortitudoincinfra_proxy.tar.bz2 -C /volume ./
```

## Restore

```bash
docker run -it --rm -v fortitudoincinfra_openmrs-database:/volume -v /home/ubuntu/volumes:/backup alpine sh -c "rm -rf /volume/* /volume/..?* /volume/.[!.]* ; tar -C /volume/ -xjf /backup/fortitudoincinfra_openmrs-database.tar.bz2"
```