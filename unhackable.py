# import lxml
import pandas as pd
import requests
from bs4 import BeautifulSoup
from icecream import ic


calc_url = 'https://app.cloud-logon.com/dev/calculator'

page = requests.get(calc_url)
ic(page.status_code)
ic(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
ic(soup.prettify())
# print(soup.find_all('h1'))
# print(soup.find_all('h1')[2].get_text())

c = pd.read_csv(calc_url)
# ic(c)
print(c)

url_hint = 'https://app.cloud-logon.com/dev/easy_mode'
page = requests.get(url_hint)
ic(page.text)

