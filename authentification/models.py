from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUSBCRIBER = "SUSCRIBER"
    ROLE_choices = (
        (CREATOR, "creator"),
        (SUSBCRIBER, "susbcriber")
    )
    profile_photo = models.ImageField(verbose_name="Photo profile", null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_choices, verbose_name="Rôle")
