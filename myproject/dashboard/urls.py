from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_categories,name='add_categories'),
    path('categories/edit/<int:pk>',views.edit_categories,name='edit_categories'),
    path('categories/delete/<int:pk>',views.del_categories,name='del_categories'),
    path('post/',views.post,name='post'),
    path('post/add/',views.add_post,name='add_post'),
    path('post/edit/<int:pk>',views.edit_post,name='edit_post'),
    path('post/delete/<int:pk>',views.del_post,name='del_post'),
    path('users/',views.users,name='users'),
    path('users/add/',views.add_user,name='add_user'),
    path('users/edit/<int:pk>',views.edit_user,name='edit_user'),
    path('users/delete/<int:pk>',views.del_user,name='del_user')
]