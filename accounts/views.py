# -*- coding: utf-8 -*-

from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, SigninForm, EditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SigninFormView(View):
    form_class = SigninForm
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()
            login(request, form.save())
            return redirect('accounts:profile')

        else:
            return render(request, self.template_name, {'form': form})



class LoginFormView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:profile')

        else:
            return render(request, self.template_name, {'form': form})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class ProfileView(View):

    template_name = 'accounts/profile.html'

    def get(self, request):
        return render(request, self.template_name)


class EditProfileView(View):

    template_name = 'accounts/editprofile.html'

    def post(self, request):
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    def get(self, request):
        form = EditForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

class ChangePassword(LoginRequiredMixin, View):
    template_name = 'accounts/change-password.html'

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)    # (form.user)  allows us to log-in the user that just change its password
                                                            # request.user was not use since currenty it is set to anonymous since it logged out the current user
            return redirect('/account/profile')

        else:
            return redirect('/account/change-password')

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form': form})


