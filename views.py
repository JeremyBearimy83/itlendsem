from django.shortcuts import render
from .models import BlogModel, BlogForm
from django.http import HttpResponseRedirect

# Create your views here.
def getBlogs(request):
    blogs = BlogModel.objects.all()
    form = BlogForm()
    context = {"blogs": blogs, "form":form}
    return render(request, "seeBlogs.html", context)

def createBlog(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        blog = form.save()
        blog.save()
    blogs = BlogModel.objects.all()
    form = BlogForm()
    context = {"blogs": blogs, "form":form}
    return HttpResponseRedirect('/blogs/')





