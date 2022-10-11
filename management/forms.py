from django import forms

from django_summernote.widgets import SummernoteWidget

from products.models import Product, Category
from blog.models import Post, PostCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 5
        self.fields['price'].widget.attrs['min'] = 0
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-styling'


class AddPostForm(forms.ModelForm):

    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = (
            'title',
            'category',
            'content',
            'featured_image',
            'status',
            'excerpt'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = PostCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-styling'
