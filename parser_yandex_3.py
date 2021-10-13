from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/news?msid=1634110651.18374.82664.102319&mlid=1634110139.glob_225&utm_medium=topnews_news'
page = requests.get(url)
filtered_news = []
all_news = []
soup = BeautifulSoup(page.text, 'lxml')

body = soup.body
div = body.findAll('div', class_='mg-grid__row mg-grid__row_gap_8')
for i in div:
    print(i.find('span', class_='mg-card-source__time').getText(),':',i.find('a', class_='mg-card__source-link').get('aria-label').replace('Источник: ',''),'==> ',i.find('h2').get_text())