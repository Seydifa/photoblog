from django.db import models
from authentification.models import User


def user_photo_path(instance, filename):
    return f"static/Images/Photos/{instance.uploader.id}/{filename}"


class Photo(models.Model):
    image = models.ImageField(upload_to=user_photo_path)
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    autheur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
