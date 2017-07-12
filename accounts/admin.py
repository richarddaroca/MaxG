# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, Album

# Register your models here.


admin.site.register(Album)
<<<<<<< Updated upstream

admin.site.register(UserProfile)




# # need to fix bug first userprofile object
# #
# # https://www.youtube.com/watch?v=KqbvhPLGJwA&index=38&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
=======

admin.site.register(UserProfile)




# need to fix bug first userprofile object

# https://www.youtube.com/watch?v=KqbvhPLGJwA&index=38&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
>>>>>>> Stashed changes
#
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'user_info', 'city', 'website', 'phone')
#
#     def user_info(self, obj):           # this is used if we want to customize the header of the column
#         return obj.description      # obj is the current object and description is the the column name
#
# # https://www.youtube.com/watch?v=j-CCNJmZQ6c&index=39&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
# # get_queryset is inherited form the ModelAdmin class
#
#     def get_queryset(self, request):    # this customizes the order on how the objects are displayed
# # since we still want to use the default get_queryset inherited on ModelAdmin we use the "super(UserProfileAdmin, self)"
#         queryset = super(UserProfileAdmin, self).get_queryset(request)
#         queryset = queryset.order_by('phone', 'user')
#         return queryset
#
#     user_info.short_description = 'Info'    # We can use this to overwrite the header name instead of using the method name
#
# admin.site.register(UserProfile, UserProfileAdmin)
