from django.db import models


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
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
    features = models.ForeignKey(
        'ProductFeature', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='feature_set')


    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    featur_1 = models.TextField(max_length=100, null=True, blank=True)
    featur_2 = models.TextField(max_length=100, null=True, blank=True)
    featur_3 = models.TextField(max_length=100, null=True, blank=True)
    featur_4 = models.TextField(max_length=100, null=True, blank=True)
    featur_5 = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.product}"