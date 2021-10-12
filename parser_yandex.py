import lxml
import requests
from bs4 import BeautifulSoup
import time

while True:

    base = 'https://yandex.ru'
    html = requests.get(base).content
    soup = BeautifulSoup(html,'lxml')
    div = soup.find('div', class_ = 'news__panel mix-tabber-slide2__panel')
    ol = div.find('ol', class_ = 'list news__list')
    a = ol.find_all('a', class_ = 'home-link2 news__item list__item-content list__item-content_with-icon home-link2_color_inherit home-link2_hover_red')
    s_new = ''
    s_old = ''
    l = []
    l_old = []
    for _ in a:
        s_new += str(_.getText()) + '\n'

    if s_new != s_old:
        s_old = s_new
        print(time.ctime())
        print(s_old)

    time.sleep(15)
