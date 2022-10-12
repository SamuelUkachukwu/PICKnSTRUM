from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<slug:slug>/', views.view_blog_article, name='view_post'),
    path('like/<slug:slug>/', views.PostLikes.as_view(), name='post_likes'),
    path(
        'dislike/<slug:slug>/',
        views.PostDislikes.as_view(),
        name='post_dislikes'
        ),
]
