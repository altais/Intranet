#-*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from news.models import Article

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'news/accueil.html', locals())

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'news/lire.html', locals())