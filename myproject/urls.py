"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import re_path
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from boards import views as boards_views
from accounts import views as accounts_views
from lectures import views as lectures_views
from about import views as about_views
from news import views as news_views

urlpatterns = [
    re_path(r'^$', boards_views.home, name='home'),
    path('lectures/', lectures_views.lectures, name='lectures'),
    path('signup/', accounts_views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('boards/', boards_views.boards, name='boards'),
    path('boards/<int:pk>/', boards_views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', boards_views.new_topic, name='new_topic'),
    path('about/', about_views.about, name='about'),
    path('news/', news_views.news, name='news'),
    path('news/global/', news_views.globalnews, name='globalnews'),
    path('api/news/', news_views.article_list),
    path('api/news/<int:pk>/', news_views.article_detail),
    path('token-auth/', obtain_jwt_token),
]
