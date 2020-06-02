from django.shortcuts import render
from home.models import ArticleToRead
from home.models import Category
from accounts.models import *
from django.http.response import HttpResponseRedirect


def settings(request):
    articles = reversed(list(ArticleToRead.objects.all()))
    categories = Category.objects.all()
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            values = request.POST.getlist('choices')
            print(values)
            user = CustomUser.objects.get(pk=request.user.pk)

            user.hi_tech = False
            user.sci_fi = False
            user.media = False
            user.psychology = False
            user.history = False
            user.biology = False
            user.medicine =False
            user.physics = False
            user.cosmology = False
            user.save()

            for val in values:
                if val == 'Hi-Tech':
                    user.hi_tech=True
                elif val == 'Sci-Fi':
                    user.sci_fi=True
                elif val == 'Медиа':
                    user.media =True
                elif val == 'Психология':
                    user.psychology=True
                elif val == 'История':
                    user.history=True
                elif val == 'Биология':
                    user.biology=True
                elif val == 'Медицина':
                    user.medicine=True
                elif val == 'Физика':
                    user.physics=True
                elif val == 'Космонавтика':
                    user.cosmology=True

                user.save()
                print(user)

        return render(request, 'article/settings.html', locals())
    else:
        return HttpResponseRedirect('/login/')
