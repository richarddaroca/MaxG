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


class Friend(models.Model):
    # When 2 or more types of relationship such as ManyToMany, ForeignKey are
    # used in a model. Django would require a related name for the others.
    # default value: related_name = <class_name>_set

    users = models.ManyToManyField(User)
    # current_user is the owner of the friends list
    # null = True can be removed if we don't have an object of friend in the database * during implementation
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)


    @classmethod
    def unfriend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

