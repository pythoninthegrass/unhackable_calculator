import requests
from bs4 import BeautifulSoup

base_url = 'https://app.cloud-logon.com/dev/'

get_calc_url = base_url + "calculator"
get_hint_url = base_url + "easy_mode"

main_page = requests.get(get_calc_url)
main_page_soup = BeautifulSoup(main_page.text, 'html.parser')
print(f"MAIN PAGE\n\n\n{main_page_soup}")
# To-Do: extract AWS account number

hint_page = requests.get(get_hint_url)
hint_page_soup = BeautifulSoup(hint_page.text, 'html.parser')
print(f"HINT PAGE\n\n\n{hint_page_soup}")
# To-Do: add Debug=True to POST body for do_math
