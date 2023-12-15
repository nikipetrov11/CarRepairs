from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render


# Предполага се, че имате собствена форма за логин

def login_view(request):
    if request.method == 'POST':
        # Обработка на формата за вход
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Влизане успешно, пренасочване към началната страница или друга страница
            return redirect('index.html')  # Променете 'home' с името на вашата начална страница
        else:
            # Невалиден вход, може да покажете грешка или пренасочите към същата страница за вход
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    else:
        # Показване на страницата за вход (можете да имате собствен шаблон за вход)
        return render(request, 'login.html')
