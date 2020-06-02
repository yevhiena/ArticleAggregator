from django.contrib import admin
from django.urls import path
from django.urls import include, path
from home import views



urlpatterns = [

    path('', views.home, name ='home'),
    path('about/', views.about,  name ='about'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('<path:name_category>/', views.Category_pages, name ='Category_pages'),



]
