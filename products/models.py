from django.db import models
from django.contrib.auth.models import User


RATES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


# Create your models here.
class Category(models.Model):
    """Groups Products into categories"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    features = models.ManyToManyField(
        'ProductFeature', blank=True, related_name='feature_set')

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    """Adds features to product model"""
    title = models.TextField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """Review can be added to product model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=254)
    rate = models.IntegerField(choices=RATES)
    updated_on = updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review by {self.name} verified purchase"
