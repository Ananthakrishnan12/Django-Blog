from enum import auto
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Blog, Category
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_post=Blog.objects.filter(is_featured=True,status="Published").order_by("updated_at")
    posts=Blog.objects.filter(is_featured=False,status="Published")
    context={
        "featured_post":featured_post,
        "posts":posts,
    }
    return render(request,"home.html",context)


def register(request):
    if request.method=="POST":
        forms=RegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('register')
    else:
        forms=RegistrationForm()
    context={
        "form":forms,
    }
    return render(request,"register.html",context)

def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect("dashboard")
    forms=AuthenticationForm()
    context={
        "forms":forms,
    }
    return render(request,"login.html",context)

def logout(request):
    auth.logout(request)
    return redirect('home')
