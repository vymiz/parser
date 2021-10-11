import lxml
import requests
from bs4 import BeautifulSoup

base = 'https://www.python.org'
html = requests.get(base).content
soup = BeautifulSoup(html,'lxml')
div = soup.find('div', class_ = 'shrubbery')
menu = div.find_all('ul', class_ = 'menu')
# print(menu)
for _ in menu:
    print(_.getText())

# print(_)