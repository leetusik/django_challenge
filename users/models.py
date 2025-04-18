from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=255, editable=False)
    last_name = models.CharField(max_length=255, editable=False)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
