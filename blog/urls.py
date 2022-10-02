from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<slug:slug>/', views.view_blog_article, name='view_post'),
]
