import time
import requests
import operator

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article
from .newsscraper import newsapi
from .serializers import *

def news(request):
    keywords = ['climate change','environment','biodiversity','pollution']
    global_news_preview = Article.objects.all().order_by('date').reverse()[:2]
    return render(request, 'news.html', {'news': global_news_preview})

def globalnews(request):
    global_news = Article.objects.order_by('date').reverse()
    paginator = Paginator(global_news,3) #Show 2 news articles per page
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'globalnews.html', {'news': articles})

# List articles or add a new article through the API
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        articles = Article.objects.order_by('date').reverse()
        page = request.GET.get('page', 1)
        paginator = Paginator(articles,2)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ArticleSerializer(data,context={'request':request},many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return(Response({'data':serializer.data, 'count':paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/news/?page=' + str(nextPage), 'prevlink': '/api/news/?page=' + str(previousPage)}))

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Retrieve update or delete an article through the API

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
