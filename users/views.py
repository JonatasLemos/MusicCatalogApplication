from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')
        if User.objects.filter(username=name).exists():
            messages.error(request, 'User already registered')
            return redirect('register')
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        messages.success(request, 'Registration performed successfully')
        return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if User.objects.filter(username=name).exists():
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                messages.warning(request,"Successfully logged in")
                return redirect('index')
        else:
            messages.warning(request,"No such user in our database,try again or register for free")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.warning(request,"Successfully logged out")
    return redirect('index')

