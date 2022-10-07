from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.management,
        name='management'),
    path(
        'add_product/',
        views.add_product,
        name='add_product'),
    path(
        'edit_product/<int:product_id>/',
        views.edit_product,
        name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete'),

]
