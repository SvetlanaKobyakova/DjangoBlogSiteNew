from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {'title': 'Главная страница'}
    return render(request, template_name='blog/index.html', context=context)

def about(request):
    context = {'title': 'О сайте'}
    return render(request, template_name='blog/about.html', context=context)
