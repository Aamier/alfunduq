from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    is_profile_updated = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta(object):
        unique_together = ('email',)

