from django.contrib import admin
from .models import Product, Category, ProductFeature


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)
    search_fields = ('sku', 'name', 'category')
    list_filter = ('sku', 'category', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ('friendly_name',)


class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductFeature, ProductFeatureAdmin)
