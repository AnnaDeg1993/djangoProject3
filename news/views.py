import asyncio
from news.bot import Base, main, engine

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *

menu = [{'title': "Обратная связь", 'url_name': 'contact'},
        ]


def index(requst):
    posts = News.objects.all()
    return render(requst, 'index.html', {'posts': posts, 'menu': menu, 'title': 'Познавательные статьи'})


@csrf_exempt
def contact(request):
    context = {'menu': menu}
    return render(request, 'contact.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(News, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'post.html', context=context)


@csrf_exempt
def reg(request):
    regi = Userform2()
    if request.method == 'POST':
        regi.email = request.POST['email']
        regi.password = request.POST['password']
        regi.save()
        return HttpResponse('Email'+' '+regi.email+' '+"успешно зарегистрирован!")
    return render(request, 'reg.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = News.objects.all()
        return render(request, 'aboutme.html')
    return render(request, 'login.html')


@csrf_exempt
def bot(request):
    if request.method == 'POST':
        print('Bot started!')
        asyncio.run(main())
    return render(request, 'contact.html')

