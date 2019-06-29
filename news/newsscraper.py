from django.shortcuts import render
import re
import json
import requests
requests.packages.urllib3.disable_warnings()
from .models import Article
#from google_images_download import google_images_download
from bs4 import BeautifulSoup

def scrape(x):
    session = requests.Session()
    url = x
    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    posts = soup.find_all('div',{'class':'fc-item__container'})

    for post in posts:
        link = post.find('a',{'class':'u-faux-block-link__overlay'})
        post_url = link['href']
        title = link.text
        print(title)

        session_post = requests.Session()
        content_post = session_post.get(post_url, verify=False).content
        soup_post = BeautifulSoup(content_post, "html.parser")

        description = soup_post.find('meta',{'itemprop':'description'})['content']
        print(description)
        post_time = soup_post.find('time',{'itemprop':'datePublished'})['datetime']
        print(post_time)
        try:
            image = soup_post.find('img',{'class':'gu-image'})['src']
        except:
            try:
                image = soup_post.find('meta',{'itemprop':'image'})['content']
            except:
                image = soup_post.find('img',{'itemprop':'contentUrl'})['src']

def newsapi():
    api_url = 'https://newsapi.org/v2/top-headlines'
    payload = {
        'apiKey':'15bfbbe422ce4505b1aba6dca0f16dce',
        'q':'climate',
        'pageSize':15,
        }
    response = requests.get(api_url, params=payload).json()
    articles = response['articles']
    for art in articles:
        print(art)
        if not Article.objects.filter(headline = art['title']).exists():
            try:
                print('jajajaja')
                new_article = Article()
                new_article.headline = art['title']
                new_article.trailtext = art['description']
                new_article.thumbnail = art['urlToImage']
                new_article.url = art['url']
                new_article.date = art['publishedAt']
                new_article.source = art['source']['name']
                new_article.save()
            except:
                continue

def theguardianAPI(keywords):
    api_url = 'http://content.guardianapis.com/environment'
    payload = {
        'api-key':'f1d636cb-37bd-46c9-8df8-594a30d48785',
        'page-size':15,
        'show-fields':'thumbnail,headline,trailText',
        }
    response = requests.get(api_url, params=payload).json()['response']
    data = response['results']
    #print(data)
    xcount = 0
    for art in data:
        headline = art['fields']['headline']
        trailtext = re.sub('<[^<]+?>', '', art['fields']['trailText'])
        thumbnail = art['fields']['thumbnail']
        weburl = art['webUrl']
        date = art['webPublicationDate']
        if not Article.objects.filter(headline = headline).exists():
            new_article = Article()
            new_article.headline, new_article.trailtext, new_article.thumbnail, new_article.url, new_article.date, new_article.source = headline, trailtext, thumbnail, weburl, date, 'The Guardian'
            new_article.save()
