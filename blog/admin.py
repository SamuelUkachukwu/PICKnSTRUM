from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models


# Register your models here.

@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'category')
    search_fields = ['author', 'content', 'title', 'category']
    list_display = ('title', 'slug', 'created_on')
    summernote_fields = ('content')


@admin.register(models.PostCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        )
