from django.shortcuts import render
from .models import Websta

# Create your views here.


def feed(request):
    posts = Websta.objects.all()
    return render(request, 'feed.html', {'posts': posts})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')
