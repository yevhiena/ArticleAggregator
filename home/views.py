from django.shortcuts import render
from home.models import ArticleToRead
from home.models import Category
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from accounts.models import CustomUser

from home.parser import import_to_db


def home(request):
    user = request.user
    if user.is_authenticated:
        articles = reversed(list(ArticleToRead.objects.all()))
        categories = Category.objects.all()
        import_to_db()
        return HttpResponse(render(request, 'article/home.html', locals()))
    else:
        return HttpResponseRedirect('/login/')

def about(request):
    user = request.user
    if user.is_authenticated:
        articles = reversed(list(ArticleToRead.objects.all()))
        categories = Category.objects.all()
        return HttpResponse(render(request, 'article/about.html', locals()))
    else:
        return HttpResponseRedirect('/login/')


def subscriptions(request):
    user=request.user
    if user.is_authenticated:
        articles = reversed(list(ArticleToRead.objects.all()))
        categories = Category.objects.all()
        user = CustomUser.objects.get(pk=request.user.pk)
        return render(request, 'article/Subscriptions.html', locals())
    else:
        return HttpResponseRedirect('/login/')



def Category_pages(request, name_category):
    articles = reversed(list(ArticleToRead.objects.all()))
    categories = Category.objects.all()
    user = request.user
    if user.is_authenticated:
        if name_category == 'Hi-Tech':
            return HttpResponse(render(request, 'categories/Hi-Tech.html', locals()))
        elif name_category == 'Sci-Fi':
            return HttpResponse(render(request, 'categories/Sci-Fi.html', locals()))
        elif name_category == 'Психология':
            return HttpResponse(render(request, 'categories/Psyсhology.html', locals()))
        elif name_category == 'История':
            return HttpResponse(render(request, 'categories/History.html', locals()))
        elif name_category == 'Медицина':
            return HttpResponse(render(request, 'categories/Medicine.html', locals()))
        elif name_category == 'Медиа':
            return HttpResponse(render(request, 'categories/Media.html', locals()))
        elif name_category == 'Биология':
            return HttpResponse(render(request, 'categories/Biology.html', locals()))
        elif name_category == 'Физика':
            return HttpResponse(render(request, 'categories/Physics.html', locals()))
        elif name_category == 'Космонавтика':
            return HttpResponse(render(request, 'categories/Cosmology.html', locals()))
    else:
        return HttpResponseRedirect('/login/')


