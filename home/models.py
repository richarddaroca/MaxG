# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
# auto_now_add=True (only saves a date once) rather than auto_now=True which WILL also update on subsequent saves.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post
