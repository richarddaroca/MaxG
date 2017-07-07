# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

# https://www.youtube.com/watch?v=484iSmV3l80&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=40
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city = 'cdo')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    cdo = UserProfileManager()

    def __str__(self):
        return self.user.username

# this code allows you to add the UserProfile into the built in User
def create_profile(sender, **kwargs):
    if kwargs['created']:  # when the user creates a new User it would create user_profile
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title



