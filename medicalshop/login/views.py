from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


# Create your views here.
def signupuser(request):
    # There are two types of request GET and POST, GET - when user enters the url in browser, or simply
    # navigates to that page. POST - Always when user submits the form.
    # Instead of signup.html we can also use UuserCreationForm provided by Django,
    # imported from django.contrib.auth.forms
    if request.method == 'GET':
        return render(request, 'login/signup.html')
    else:
        # Create a new user
        if request.POST['password'] == request.POST['re_password']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                                email=request.POST['email'])
                user.save()
                login(request,user)
                return redirect(to='medicine')
            except IntegrityError:
                return render(request, 'login/signup.html', {
                    'userAlreadyExistsError': "That username has already been taken! Please choose a new one."})

        else:
            return render(request, 'login/signup.html', {'passwordMismatchError': 'Password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        user = authenticate(request, username= request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request,'login/login.html',{'userNotExistsError': 'User with provided credentials does not exists!'})
        else:
            login(request, user)
            return redirect(to='medicine')


def logoutuser(request):
    #Checking this is very important because when Chrome or some browsers actually start loading the web pages
    #to make user interaction faster, it may happen as soon as the user logegd in and logout link appear
    #chrome makes a request and logges out the user. we have to keep in mind that we should only log out the user when it
    #is a POST request
    if request.method == "POST":
        logout(request)
        return redirect('home')