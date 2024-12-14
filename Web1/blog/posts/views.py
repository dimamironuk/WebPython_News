from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  
    form = PostForm(request.POST or None)
    
    if request.method == 'POST':  
        if form.is_valid():
            form.save()  
            return redirect('post_list') 

    return render(request, 'posts_list.html', {'posts': posts, 'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
