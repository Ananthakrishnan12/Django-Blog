from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog,Category

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
