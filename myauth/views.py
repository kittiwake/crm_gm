from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('timetable')
        
        return render(request, 'myauth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect('timetable')
    
    return render(request, 'myauth/login.html', {'error': 'Неверный пользователь или пароль'})


