from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', { 'posts':posts })

def new(request):
    if request.method == 'POST':
        forms = PostForm(request.POST, request.FILES)
        post = forms.save(commit=False)
        post.save()

        return redirect('detail', post.pk)
    else:
        form = PostForm()

        return render(request, 'new.html', { 'form':form })

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', { 'post':post })