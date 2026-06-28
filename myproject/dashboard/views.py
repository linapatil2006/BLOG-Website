from django.shortcuts import render,redirect
from myapp .models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm,UserForm,EditUserForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'category_count':category_count,
        'blog_count':blog_count
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')


def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(request,'dashboard/add_categories.html',{'form':form})


def edit_categories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method =='POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }
    return render(request,'dashboard/edit_categories.html',context)



def del_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')





def post(request):
    post = Blog.objects.all()
    context = {
        'post':post
    }
    return render(request,'dashboard/post.html',context)

def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            form.save()
            title = form.cleaned_data['title']
            posts.slug = slugify(title)
            posts.save()
            return redirect('post')
    else:
        form = BlogForm()
        
    context = {
        'form':form
    }
    return render(request,'dashboard/add_post.html',context)




def edit_post(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method =='POST':
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = BlogForm(instance=blog)
    context = {
        'form':form,
        'blog':blog
    }
    return render(request,'dashboard/edit_post.html',context)




def del_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('post')



def users(request):
    users = User.objects.all()
    return render(request,'dashboard/users.html',{'users':users})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request,'dashboard/add_user.html',{'form':form})


def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method =='POST':
        form = EditUserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)
    context = {
        'form':form,
        'user':user
    }
    return render(request,'dashboard/edit_user.html',context)

def del_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')