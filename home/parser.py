import requests
from bs4 import BeautifulSoup
from home.models import *



URL = 'https://naked-science.ru/article/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'accept': '*/*'}



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(art):
    articles = []
    count=0
    for article in art:

        if article.find('div', class_='terms-item terms-item--cat') == None:
            continue
        if article.find('div', class_='terms-item terms-item--cat').find_next('a').get_text() == 'FAQ':
            continue
        count += 1
        if count==20:
            break

        ref = article.find('div', class_='news-item-title').find_next('a').get('href')
        html = get_html(ref)
        soup = BeautifulSoup(html.text, 'html.parser')
        single = soup.find('div', class_='content')

        body=single.find('div', class_='body').find_all('p')


        for i in range(len(body)):
            body[i]= body[i].get_text()
        BODY= ''.join(body)


        articles.append({
            'title': single.find('div', class_='post-title').find_next('h1').get_text(),
            'link': single.find('div', class_='post-title').find_next('a').get('href'),
            'author':   single.find('div', class_='meta-item meta-item_author').get_text(),
            'category':  single.find('div', class_='terms-item terms-item--cat').find_next('a').get_text(),
            'body': BODY,

        })

    return articles


def parse():
    html = get_html(URL)
    if html.status_code==200:
        soup = BeautifulSoup(html.text, 'html.parser')
        art = soup.find_all('div', class_='news-item grid')
        all =get_content(art)
        return all
    else:
        print('error')

all=parse()

def import_to_db():
    already_in_db = ArticleToRead.objects.all()
    categ= Category.objects.all()

    for one in all:
         check_indb = 1
         check_categ = 0
         for indb in already_in_db:
            if one.get('title')==indb.name:
                check_indb=0

         for cat in categ:
             if one.get('category')==cat.name_category:
                 check_categ=1

         if check_indb and check_categ:
             data = ArticleToRead(name=one.get('title'), body=one.get('body'), author=one.get('author'),
                                 category=one.get('category'))
             data.save()

