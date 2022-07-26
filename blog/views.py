from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request,'index.html',{'post_list': posts})

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html',{'post':post})