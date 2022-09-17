from django.contrib.auth.models import AbstractUser
from django.db import models


def user_profile_path(instance, filename):
    return f"static/Images/Profiles/{instance.id}/{filename}"


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUSBCRIBER = "SUSCRIBER"
    ROLE_choices = (
        (CREATOR, "creator"),
        (SUSBCRIBER, "susbcriber")
    )
    profile_photo = models.ImageField(upload_to=user_profile_path, verbose_name="Photo profile",
                                      null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_choices, verbose_name="Rôle")
