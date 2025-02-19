from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog,Category
from django.db.models import Q

def post_by_category(request,category_id):
    # Fetch the post that belongs to the category with the category_id.
    posts=Blog.objects.filter(status="Published",category_id=category_id)
    # use try/except when we want to some custom action if the category does not exsists.
    try:
        category=Category.objects.get(pk=category_id)
    except:
        return redirect("home")
    #Use get_object_or_404 when you want to show 404 error page if the necessary category does not exsists.
    # category=get_object_or_404(Category,pk=category_id)
    context={
        "posts":posts,
        "category":category,
    }
    return render(request,"post_by_category.html",context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug)
    context={
        "single_blog":single_blog,
    }
    return render(request,"blogs.html",context)


def search(request):
    keyword=request.GET.get("keyword")
    blogs=Blog.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword))
    context={
        "blogs":blogs,
        "keyword":keyword,
    }
    return render(request,"search.html",context)