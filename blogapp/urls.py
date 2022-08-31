from django.urls import path
from blogapp.apps import BlogappConfig
from blogapp import views

app_name = BlogappConfig.name

urlpatterns = [
    path('', views.blog, name='blog'),
]

