from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.core.exceptions import PermissionDenied

# Create your views here.

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/lista_posts.html', {'posts':posts})


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html' , {'post':post})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registro.html', {'form': form})


@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'titulo_pagina': 'Nuevo post'})


@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'titulo_pagina': 'Editar post'})



@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'blog/post_confirmar_eliminar.html', {'post': post})


