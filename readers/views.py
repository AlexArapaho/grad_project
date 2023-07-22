from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def register_reader(request):
    page = 'register'
    context = {
        'page': page,
        'form': UserCreationForm()
    }
    if request.method == "GET":
        return render(request, 'readers/login_register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'readers/login_register.html', context,
                                  {'error': 'Такое имя уже существует'})

        else:
            return render(request, 'readers/login_register.html', context,
            {'error': 'Пароли не совпадают'})
    # if request.method == "GET":
    #     return render(request, 'readers/login_register.html', {'form': UserCreationForm()})
    # else:
    #     if request.POST['password1'] == request.POST['password2']:
    #         try:
    #             user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
    #             user.save()
    #             login(request, user)
    #             return redirect('profile')
    #         except IntegrityError:
    #             return render(request, 'readers/login_register.html', {'form': UserCreationForm()},
    #                               {'error': 'Такое имя уже существует'})
    #
    #     else:
    #         return render(request, 'readers/login_ register.html', {'form': UserCreationForm()},
    #         {'error': 'Пароли не совпадают'})


def login_reader(request):
    if request.method == 'GET':
        return render(request, 'readers/login_register.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'readers/login_register.html', {'form': AuthenticationForm(), 'error': "Неверные данные для входа"})
        else:
            login(request, user)
            return redirect("index")

def logout_reader(request):
    logout(request)
    return redirect('index')


def profile(request, pk):
    prof = Profile.objects.get(id=pk)

    return render(request, 'readers/profile.html', {'profile': prof})