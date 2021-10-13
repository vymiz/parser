from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru'
page = requests.get(url)
filtered_news = []
all_news = []
# soup = BeautifulSoup(page.text, 'html.parser')
soup = BeautifulSoup(page.text, 'lxml')

txt = []
ol = soup.ol
a = ol.find_all('a')
for _ in a:
    txt.append((_.get('aria-label')))

title = []
div = ol.find_all('div')
for _ in div:
    title.append((_.get('title')))

res = []
for i in range(len(txt)):
    s = title[i] + ': ' + txt[i]
    res.append(s)

for i in res:
    print(i)

'''
li = soup.div.ol.find_all('li')
for _ in li:
    ttl = _.find('div')
    txt = _.find('a')
    print(ttl['title'], "==> ", txt['aria-label'])

'''
