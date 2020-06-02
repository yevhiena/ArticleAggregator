from django.urls import include, path
from accounts import views



urlpatterns = [

    path('login/', views.LoginFormView.as_view(), name ='auth'),
    path('singup/', views.RegisterFormView.as_view(), name='reg'),
    path('login/', views.LogoutView,  name ='logout'),
]