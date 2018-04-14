#!/usr/bin/env python3

import requests
import sys
import json
import getpass

OPENMRS_SITE = "https://openmrs.callnigeriandoc.com"

def usage():
    print("Usage: {} /path/to/users.json".format(sys.argv[0]))
    
def main(filename):
    with open(filename, 'r') as f:
        users = json.load(f)
        
    admin_password = getpass.getpass("Admin password:")
    sess = requests.session()
    
    # Login
    resp = sess.post(OPENMRS_SITE + "/openmrs/login.htm", data={
        "username": "Admin",
        "password": admin_password,
        "sessionLocation": 6
    })
    
    if resp.status_code != 200:
        print("failed to log in")
        quit()
    
    for user in users:
        user_data = {
            "createNewPerson": True,
            "person.names[0].givenName": user["firstname"],
            "person.names[0].middleName": user["middlename"],
            "person.names[0].familyName": user["lastname"],
            "person.gender": user["gender"],
            "providerCheckBox": user["provideraccount"],
            "username": user["username"],
            "userFormPassword": user["password"],
            "confirm": user["password"],
            "forcePassword": user["forcepasschange"],
            "roleStrings": user["role"]    
        }
        
        resp = sess.post(OPENMRS_SITE + "/openmrs/admin/users/user.form", data=user_data)
        print(resp.text)
        
        if(resp.status_code != 200):
            quit()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    else:
        main(sys.argv[1])