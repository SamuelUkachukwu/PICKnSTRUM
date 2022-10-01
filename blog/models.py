from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Published'))


class PostCategory(models.Model):
    """Model groups posts into categories"""
    class Meta:
        verbose_name_plural = 'PostCategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    """Blod post model"""
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        PostCategory, null=True, on_delete=models.SET_NULL, related_name='post')
    content = models.TextField()
    featured_image = models.URLField(max_length=1024, null=True, blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='story_likes', blank=True
        )
    dislikes = models.ManyToManyField(
        User, related_name='story_dislikes', blank=True
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()