from django.shortcuts import render, redirect, get_object_or_404
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


def new(request):
    return render(request, 'new.html')


def create(request):
    new_post = Websta()
    new_post.writer = request.POST['writer']
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('feed')


def edit(request, id):
    edit_post = Websta.objects.get(id=id)
    return render(request, 'edit.html', {'post': edit_post})


def update(request, id):
    update_post = Websta.objects.get(id=id)
    update_post.writer = request.POST['writer']
    update_post.image = request.FILES['image']
    update_post.save()
    return redirect('feed')


def delete(request, id):
    delete_post = Websta.objects.get(id=id)
    delete_post.delete()
    return redirect('feed')
