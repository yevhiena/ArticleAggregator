from django.urls import include, path
from settings import views



urlpatterns = [

    path('', views.settings, name ='settings' ),

]