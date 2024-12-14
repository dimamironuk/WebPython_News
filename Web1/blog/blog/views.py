from django.shortcuts import redirect, render
from posts.forms import PostForm
from posts.models import Post

def homepage(request):
    posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'home.html', {'posts': posts})  


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
