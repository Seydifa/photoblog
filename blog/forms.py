from django import forms
from blog.models import Photo, Blog


class Photoform(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', "caption")


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]
