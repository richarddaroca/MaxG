# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from home.forms import HomeForm
from home.models import Post
from django.contrib.auth.models import User




class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        post = Post.objects.all().order_by('-created') #orders the post by date created
        users = User.objects.exclude(id=request.user.id)

        args = {'form': form, 'post': post, 'users': users}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
#https://www.youtube.com/watch?v=qwE9TFNub84&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=47
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user            # this says that the post is save on the current user
            post.save()

            text = form.cleaned_data['post']    #'post' is the varialble we named it on forms.py
            form = HomeForm()                   # This is just here so that after we hit submit the text field will be empty
            return redirect('/home')       # since it would instantiate another object

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)











