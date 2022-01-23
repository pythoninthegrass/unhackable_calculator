# import lxml
import pandas as pd
import re
import requests
import requests_cache
from bs4 import BeautifulSoup
from icecream import ic

base_url = 'https://app.cloud-logon.com/dev/'
calc_url = base_url + "calculator"
hint_url = base_url + "easy_mode"

requests_cache.install_cache('main_page_cache')
main_page = requests.get(calc_url)

# TODO: extract AWS account number
main_page_soup = BeautifulSoup(main_page.text, 'html.parser')
print(f"MAIN PAGE\n\n{main_page_soup}")
ic(main_page_soup.prettify())
# print(soup.find_all('h1'))
# print(soup.find_all('h1')[2].get_text())

c = pd.read_csv(calc_url)
print(c)

hint_page = requests.get(hint_url)
hint_page_soup = BeautifulSoup(hint_page.text, 'html.parser')
print(f"HINT PAGE\n\n{hint_page_soup}")
ic(hint_page.text)
