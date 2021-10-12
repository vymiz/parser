import lxml
import requests
from bs4 import BeautifulSoup

base = 'https://www.python.org'
html = requests.get(base).content
soup = BeautifulSoup(html,'lxml')
div = soup.find('div', class_ = 'shrubbery')
menu = div.find('ul', class_ = 'menu')


# this part of code works properly
l1 = []
for _ in menu.find_all('a'):
    l1.append(((_.get_text())))#, ' ', _.get('href')))

l2 = []
for _ in menu.find_all('time'):
    l2.append(((_.get_text())))

s = ''
for i in range(len(l1)):
    s += l2[i] + ': ' + l1[i] + '\n'

print(s)