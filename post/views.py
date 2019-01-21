from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm, CommentModelForm

# Create your views here.

def index(request):
    context = {}
    context['posts'] = Post.objects.all()
    return render(request, 'index.html', context)

def details(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    context['comment'] = CommentModelForm(initial={'post':Post.objects.get(id=post_id)})

    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'details.html', context)
    else:
        return render(request, 'details.html', context)

    return render(request, 'details.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            context['form']  = form
            return render(request, 'update.html', context)

    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'update.html', context)

def add(request):
    context = {}
    context['form'] = PostModelForm(initial={'is_active':True})
    
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else: 
            return render(request, 'add.html', context)
    else:
        return render(request, 'add.html', context)
