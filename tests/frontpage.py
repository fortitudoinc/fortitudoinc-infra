#!/usr/bin/env python3

import requests
import sys

from bs4 import BeautifulSoup

BASE_URL = "http://localhost:8080/openmrs"

content = requests.get(BASE_URL).text
soup = BeautifulSoup(content, "html.parser")
assert soup != None