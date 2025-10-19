from django.shortcuts import render,redirect
from django.http import request
from .models import Blog
from .forms import blogForm

def blog(request,pk):
    blog = Blog.objects.get(id=pk)
    return render(request,'app/blog.html',{'blog':blog})

def main(request):
    blogs = Blog.objects.all()
    return render(request,'app/main.html',{'blogs':blogs})

def update(request,pk):
    blog = Blog.objects.get(id=pk)
    form = blogForm(instance=blog)
    if request.method == 'POST':
        form = blogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request,'app/form.html',{'form':form})

def delete(request,pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('admin')
    return render(request,'app/delete.html',{'blog':blog})

def admin(request):
    blogs = Blog.objects.all()
    return render(request,'app/admin.html',{'blogs':blogs})

def create(request):
    form = blogForm()
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request,'app/form.html',{'form':form})