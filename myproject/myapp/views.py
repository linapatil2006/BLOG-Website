from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Category,Blog,Comments
from django.shortcuts import get_object_or_404
from django.db.models import Q
from . forms import RegistrationForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_feacherd=True, status='published')
    posts = Blog.objects.filter(is_feacherd=False, status='published')
   
    context = {
        'categories':categories,
        'featured_post':featured_post,
        'posts':posts
    }
    return render(request,'home.html', context)


def posts_by_category(request,category_id):
    posts = Blog.objects.filter(status='published',category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html', context)


def blogs(request,slug):
    single_post = get_object_or_404(Blog,slug=slug , status ='published')
    # comment from browser 
    com = Comments()
    if request.method == 'POST':   
        com.user = request.user
        com.blog = single_post
        com.comment = request.POST['comment']
        com.save()
        return HttpResponseRedirect(request.path_info)

    #for commenting
    comment = Comments.objects.filter(blog = single_post)
    comment_count = comment.count()

    context = {
        'single_post':single_post,
        'comment':comment,
        'comment_count':comment_count
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')
    blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword)  |  Q(blog_body__icontains=keyword),status ='published')
    content = {
        'blog':blog,
        'keyword':keyword
    }
    return render(request,'search.html',content)


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()

    context={
        'form':form
    }
    return render(request,'register.html',context)

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username , password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }
    return render(request, 'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')