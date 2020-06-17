from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    date_of_birth = models.DateField(default=date.today)
