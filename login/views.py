from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'login/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password != c_password:
            messages.error(request, "Passwords is not equals")
            return redirect('signup')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname

            myuser.save()

            messages.success(request, "Your account has successfully created!")

        return redirect("signin")

    return render(request, 'login/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            username = user.first_name
            return render(request, 'login/index.html', {'username':username})
        else:
            messages.error(request, 'Bad credentials! Verify username and password.')
            return redirect('signin')

    return render(request, 'login/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out successfully!")
    return redirect('home')
