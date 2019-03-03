#!/usr/bin/env python3

import requests
import time
import sys

from bs4 import BeautifulSoup

"""
Wait for refapp to be ready, fail if exceed TIMEOUT # of attempts
"""

BASE_URL = "http://localhost:8080/openmrs"
TIMEOUT = 100

attempts = 0
ready = False

def handle_timeout():
    sys.exit("Timeout exceeded")


while not ready:
    try:
        content = requests.get(BASE_URL).text
        soup = BeautifulSoup(content, "html.parser")
        if soup.title and soup.title.get_text() == "Login":
            print("[+] Detected refapp in ready state")
            ready = True
        else:
            attempts += 1
            time.sleep(1)
            print("[*] Waiting on refapp to get to ready state...".format(attempts, TIMEOUT))

    except requests.exceptions.ConnectionError:
        attempts += 1
        time.sleep(1)
        print("[-] Waiting for refapp to open socket, attempt {}/{}...".format(attempts, TIMEOUT))

    
    if attempts > TIMEOUT:
        handle_timeout()
    
