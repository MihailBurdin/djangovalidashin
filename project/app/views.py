from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, UserFormLogin
from .models import Person

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            return HttpResponse('Регистрация успешна!')
        else:
            return HttpResponse('Invalid data')
    else:
        form = UserForm()
        return render(request, 'register.html', context={'form': form})

def login(request):
    if request.method == 'POST':
        userform = UserFormLogin(request.POST)
        if userform.is_valid():
            return HttpResponse('Вход успешен!')
        else:
            return redirect('/signup')
    else:
        form = UserFormLogin()
        return render(request, 'login.html', context={'form': form})

