import requests
import lxml
from bs4 import BeautifulSoup

base = 'https://ru.stackoverflow.com'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id = 'question-mini-list')
# print(div)
a = div.find_all('a', class_ = 'question-hyperlink')
print(len(a))
for _ in a:
    print(_.getText(), '\t', base + _.get('href'), '\n'*2)