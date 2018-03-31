#!/usr/bin/env python3

import requests
import sys

SETUP_URL = 'http://localhost:8080/openmrs/initialsetup'

def post_wrapper(s, post_data):
    resp = s.post(SETUP_URL, data=post_data)
    assert resp.status_code == 200
    
MYSQL_HOST = sys.argv[1]
MYSQL_USER = sys.argv[2]
MYSQL_PASSWORD = sys.argv[3]
ADD_DEMO_DATA = sys.argv[4]
ADMIN_PASSWORD = sys.argv[5]
    
sess = requests.session()

# Step 1: get cookie
resp = sess.get(SETUP_URL)
assert resp.status_code == 200

# Be idempotent! Detect if site already installed
if "** NOTE TO DEVELOPERS  **" in resp.text:
    print("[*] Site appears to be installed already, skipping initial setup.")

# Step 2: set lang
post_wrapper(sess, {
    'page': 'chooselang.vm',
    'locale': 'en',
    'continue.x': 26,
    'continue.y': 46
})

# Step 3: select advanced install
post_wrapper(sess, {
    'page': 'installmethod.vm',
    'install_method': 'advanced',
    'continue.x': 29,
    'continue.y': 29
})

# Step 4: database connection setup
post_wrapper(sess, {
    'page': 'databasesetup.vm',
    'database_connection': 'jdbc:mysql://{}:3306/@DBNAME@?autoReconnect=true&sessionVariables=default_storage_engine=InnoDB&useUnicode=true&characterEncoding=UTF-8'.format(MYSQL_HOST),
    'database_driver': '',
    'openmrs_current_database_name': 'openmrs',
    'current_openmrs_database': 'no',
    'openmrs_new_database_name': 'openmrs',
    'create_database_username': MYSQL_USER,
    'create_database_password': MYSQL_PASSWORD,
    'continue.x': 21,
    'continue.y': 23
})

# Step 5: database configuration
post_wrapper(sess, {
    'page': 'databasetablesanduser.vm',
    'create_tables': 'yes',
    'add_demo_data': ADD_DEMO_DATA,
    'current_database_user': 'yes',
    'current_database_username': MYSQL_USER,
    'current_database_password': MYSQL_PASSWORD,
    'create_user_username': 'root',
    'create_user_password': '',
    'continue.x': 32,
    'continue.y': 33
})

# Step 6: configure openmrs security options
post_wrapper(sess, {
    'page': 'otherruntimeproperties.vm',
    'module_web_admin': 'no',
    'auto_update_database': 'no',
    'continue.x': 33,
    'continue.y': 35
})

# Step 7: configure openmrs admin user
post_wrapper(sess, {
    'page': 'adminusersetup.vm',
    'new_admin_password': ADMIN_PASSWORD,
    'new_admin_password_confirm': ADMIN_PASSWORD,
    'continue.x': 32,
    'continue.y': 23
})

# Setup 8: complete setup
post_wrapper(sess, {
    'page': 'wizardcomplete.vm',
    'continue.x': 37,
    'continue.y': 29
})