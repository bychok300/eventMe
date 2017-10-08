from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='Profile')
    profile_img = models.ImageField(null=True)
#     first_name = models.TextField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     city = models.CharField(max_length=30, blank=True)


