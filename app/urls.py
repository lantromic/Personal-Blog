from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('blog/<str:pk>',views.blog,name='blog'),
    path('admin/',views.admin,name='admin'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('create',views.create,name='create'),
]
