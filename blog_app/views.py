from django.shortcuts import render,get_object_or_404
from blog_app.models import Blog

# Create your views here.

def blogView(request):
    blogs=Blog.objects.order_by('-date')[:3]
    return render(request,'blog_app/blog.html',{'blogs':blogs})


def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog_app/detail.html',{'blog':blog})
