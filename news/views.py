from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(requst):
    posts = News.objects.all()
    return render(requst, 'index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(requst):
    return render(requst, 'about.html', {'menu': menu, 'title': 'О сайте'})


#def categories(requst, catid):
    #return HttpResponse(f"<h1>Статьи по категории</h1><p>{catid}</p>")


