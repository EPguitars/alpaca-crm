from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    """ Check for login """

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно авторизировались")
            return redirect('home')
        else:
            messages.success(
                request, "Произошла ошибка, проверьте данные и повторите попытку")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Вы покинули кабинет...")
    return redirect('home')