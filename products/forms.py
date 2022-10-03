from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    RATES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    rate = forms.CharField(
        widget=forms.RadioSelect(choices=RATES))

    body = forms.CharField(widget=forms.Textarea(attrs={
        "rows": 6,
        "cols": 20,
        'placeholder': 'Add a review'
        }))

    class Meta:
        model = Review
        fields = (
            'body',
            'rate',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'form-styling'
