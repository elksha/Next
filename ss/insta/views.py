from django.shortcuts import render, redirect
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileForm

# Create your views here.
def home(request):
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts':posts, 'profiles':profiles })

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect('detail', post.pk)
    else:
        form = CommentForm()
        return render(request, 'detail.html', { 'post':post, 'form':form })

def new(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.save()

        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'new.html', { 'form':form, 'profiles':profiles })

def edit(request, post_pk):
    profiles = Profile.objects.all()
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        post = form.save(commit=False)
        post.save()
        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForm(instance = post)
        return render(request, 'new.html', { 'form':form, 'profiles':profiles })

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=post_pk)
    comment.delete()
    return redirect('detail', post_pk)

def proedit(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        profile = form.save(commit=False)
        profile.save()
        return redirect('home')
    else:
        form = ProfileForm()
        return render(request, 'proedit.html', { 'form':form, 'profiles':profiles })