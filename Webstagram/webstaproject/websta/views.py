from django.shortcuts import render

# Create your views here.


def feed(request):
    return render(request, 'feed.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')
