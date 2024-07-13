from django.shortcuts import render,HttpResponse
from .models import Posts
# Create your views here.

def bloghome(request):
    allposts = Posts.objects.all()
    context = {"allPosts":allposts}
    return render(request,"blog/blog.html",context)

def blogpost(request,slug):
    post = Posts.objects.filter(slug=slug).first()
    context = {"post":post}
    return render(request,"blog/blogpost.html",context)

