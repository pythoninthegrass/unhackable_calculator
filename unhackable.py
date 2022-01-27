#!/usr/bin/env python3

import boto3
import botocore.session
import logging
import pandas as pd
import re
import requests
import requests_cache
from bs4 import BeautifulSoup, Comment
from datetime import timedelta
# from icecream import ic
from pathlib import Path

base_url = 'https://app.cloud-logon.com/dev/'
calc_url = base_url + "calculator"
hint_url = base_url + "easy_mode"

requests_cache.install_cache("pages_cache")
main_page = requests.get(calc_url)

page_soup = BeautifulSoup(main_page.text, 'html.parser')
# print(f"MAIN PAGE\n{page_soup}")

comments = page_soup.find_all(string=lambda text: isinstance(text, Comment))
print("COMMENTS")
for comment in comments:
    print(comment.strip())

comment_regex = re.compile(r'\d{12}')
raw = comment_regex.search(str(comments))
aws_account_number = raw.group(0)
print(f"AWS ACCOUNT NUMBER: {aws_account_number}")

# TODO: missing auth token
hint_page = requests.get(hint_url)
hint_page_soup = BeautifulSoup(hint_page.text, 'html.parser')
print(f"\nHINT PAGE\n{hint_page_soup}")
print(hint_page.text)
