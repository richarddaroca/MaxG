# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'