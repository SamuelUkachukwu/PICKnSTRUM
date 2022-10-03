from django import forms
from .models import UserProfile


class ProfileImageForm(forms.ModelForm):
    COVER_PHOTO = (
        ('Cool', 'Cool'),
        ('Goth', 'Goth'),
        ('Serenity', 'Serenity'),
        ('Rock', 'Rock')
        )

    cover_photo = forms.CharField(
        widget=forms.RadioSelect(choices=COVER_PHOTO))

    class Meta:
        model = UserProfile
        fields = (
            'cover_photo',
            'image',
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'form-styling'


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country'
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'form-styling'
        self.fields['default_phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['default_street_address1'].widget.attrs['placeholder'] = 'Street Address 1'
        self.fields['default_street_address2'].widget.attrs['placeholder'] = 'Street Address 2'
        self.fields['default_town_or_city'].widget.attrs['placeholder'] = 'Town or City'
        self.fields['default_county'].widget.attrs['placeholder'] = 'County, State or Locality'
        self.fields['default_postcode'].widget.attrs['placeholder'] = 'Postal Code'
