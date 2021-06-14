from django.shortcuts import render, redirect, get_object_or_404
from .models import Websta
from django.contrib.auth.models import User

# Create your views here.


def feed(request):
    posts = Websta.objects.all()
    return render(request, 'feed.html', {'posts': posts})


def profile(request, writer_id):
    writer = get_object_or_404(User, pk=writer_id)
    writer_posts = writer.post.all()
    return render(request, 'profile.html', {"writer": writer, "writer_posts": writer_posts})


def new(request):
    return render(request, 'new.html')


def create(request):
    new_post = Websta()
    new_post.writer = request.user
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('feed')


def edit(request, id):
    edit_post = Websta.objects.get(id=id)
    return render(request, 'edit.html', {'post': edit_post})


def update(request, id):
    update_post = Websta.objects.get(id=id)
    update_post.writer = request.user
    update_post.image = request.FILES['image']
    update_post.save()
    return redirect('feed')


def delete(request, id):
    delete_post = Websta.objects.get(id=id)
    delete_post.delete()
    return redirect('feed')
