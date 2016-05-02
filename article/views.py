from django.shortcuts import render,redirect
from markdown import markdown
from django.http import HttpResponse
from datetime import datetime
from models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage
import csv
# Create your views here.
#home

def homebegin(requeset):
    article = Article.objects.all()
    article_paginator = Paginator(article,3)
    return render(requeset,'base.html',{})

def home(request):
    article = Article.objects.all()
    article_paginator = Paginator(article,3)

    return render(request,'index-images.html',{'article':article})
def article_show(requeset,id):
    try:
        article = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(requeset,'articleshow.html',{'article':article})