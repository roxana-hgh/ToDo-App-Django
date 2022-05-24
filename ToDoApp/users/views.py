from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'Account created, now Log In')
            return redirect('login')
    
    return render(request, 'users/register.html',{'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username , password = password)

        if user is not None:
            login(request,user),
            return redirect('tasks')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request, 'users/login.html',)

    return render(request, 'users/login.html',)

def logoutUser(request):
    logout(request)
    return redirect('landing')

