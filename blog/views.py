from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/accounts/login/")
def create_blog(request):
    if request.method=='POST':
        create_blog_form=Create_blog(request.POST, request.FILES)
        if create_blog_form.is_valid:
            instance= create_blog_form.save(commit=False)
            instance.owner=request.user
            instance.save()
            return redirect('blog:blogs')
        else:
            return redirect('blog:create_blog')
    else:
        create_blog_form=Create_blog()
    return render(request,'blog/create_blog.html',{'create_blog_form':create_blog_form})

def blog(request):
    blogs=Create_blogs.objects.all().order_by('created')
    return render(request, 'blog/blogs.html', {'blogs':blogs})

def comments(request):
    if (request.method=='POST'):
        comment_form=Comment(request.POST)
        if comment_form.is_valid():
            comment_form.save()
    else:
        comment_form=Comment()
    return render(request, 'blog/comments.html', {'comment_form':comment_form})