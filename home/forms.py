from django import forms


class ContactUsForm(forms.Form):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))

    body = forms.CharField(widget=forms.Textarea(attrs={
        "rows": 3,
        "cols": 20,
        'placeholder': 'Your Message'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'form-styling'
