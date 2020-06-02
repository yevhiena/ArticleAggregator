from django.shortcuts import render
from django.views.generic.edit import FormView

from accounts.forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import logout





class RegisterFormView(FormView):
    form_class = CustomUserCreationForm

    success_url = "/login/"
    template_name = "accounts.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)




class LoginFormView(FormView):

    form_class = CustomUserAuthenticationForm

    template_name = "accounts.html"
    success_url = "/home/"

    def form_valid(self, form):

        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)




def LogoutView(request):

    logout(request)
    return  LoginFormView(request)