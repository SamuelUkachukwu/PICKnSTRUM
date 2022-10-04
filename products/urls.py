from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('review/<int:product_id>/', views.review, name='review'),
    path('delete/<int:product_id>/', views.delete_review, name='delete_review'),
]
