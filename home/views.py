from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Posts
# Create your views here.

def home(request):
    return render(request,"home/home.html")
def contact(request):
    
    if request.method =="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"your message has been sent")
        # print(name,phone,email,content)
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")

def search(request):
    search = request.GET["search"]
    allPosts = Posts.objects.filter(title__icontains=search)
    context = {"allPosts":allPosts}
    return render(request,"home/search.html",context)