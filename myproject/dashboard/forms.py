from django import forms
from myapp . models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields = ('title','category','blog_image','short_desc','blog_body','status','is_feacherd')

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')