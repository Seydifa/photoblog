from django import forms
from blog.models import Photo, Blog


class Photoform(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', "caption")


class Blogform(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Blog
        fields = ["title", "content"]


class DeleteBlogform(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
