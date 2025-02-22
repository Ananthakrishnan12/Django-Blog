from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboards.forms import AddUserForm, BlogForm, CategoryForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


@login_required(login_url="login")
def dashboard(request):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        "category_count":category_count,
        "blogs_count":blogs_count,
    }
    return render(request,"dashboard/dashboard.html",context)


def categories(request):
    return render(request,'dashboard/categories.html')


def add_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form=CategoryForm()
    context={
        "form":form,
    }
    return render(request,"dashboard/add_category.html",context)


def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form=CategoryForm(instance=category)
    context={
        "form":form,
        "category":category,
    }
    return render(request,"dashboard/edit_category.html",context)


def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect("categories")


def posts(request):
    posts=Blog.objects.all()
    context={
        "posts":posts,
    }
    return render(request,"dashboard/posts.html",context)


def add_posts(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            posts=form.save(commit=False)   # temporarily saving the posts.
            posts.author= request.user
            posts.save()
            title=form.cleaned_data["title"]
            posts.slug=slugify(title)+"-"+str(posts.id)
            posts.save()
            return redirect("posts")
    form=BlogForm()
    context={
        "form":form,
    }
    return render(request,"dashboard/add_posts.html",context)

def edit_posts(request,pk):
    posts=get_object_or_404(Blog,pk=pk)
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES,instance=posts)
        if form.is_valid():
            posts=form.save()
            title=form.cleaned_data["title"]
            posts.slug=slugify(title)+"-"+str(posts.id)
            posts.save()
            return redirect("posts")
    form=BlogForm(instance=posts)
    context={
        "form":form,
        "post":posts,
    }
    return render(request,"dashboard/edit_posts.html",context)
    
    
def delete_posts(request,pk):
    posts=get_object_or_404(Blog,pk=pk)
    posts.delete()
    return redirect("posts")

def users(request):
    users=User.objects.all()
    context={
        "users":users,
    }
    return render(request,"dashboard/users.html",context)


def add_users(request):
    if request.method=="POST":
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form=AddUserForm()
    context={
        "form":form,
    }
    return render(request,"dashboard/add_users.html",context)

def edit_users(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=="POST":
        form=EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")
    
    form=EditUserForm(instance=user)
    context={
        "form":form,
    }
    return render(request,"dashboard/edit_users.html",context)


def delete_users(request,pk):
    user=get_object_or_404(User,pk=pk)
    user.delete()
    return redirect("users")