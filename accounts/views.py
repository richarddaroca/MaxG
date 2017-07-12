# -*- coding: utf-8 -*-

from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, SigninForm, EditForm, EditProfileImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


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

    def get(self, request, pk=None):         # pk=none so that we even if there is no pk passed it would just post the request.user
        # this is for the  accounts: profile_with_pk
        if pk:
            user = User.objects.get(pk=pk)   # depending on the passed pk from urls.py line 14 it would get the corresponding user
        else:
            user = request.user

        return render(request, self.template_name, {'user': user})


class EditProfileView(View):

    template_name = 'accounts/editprofile.html'

    def post(self, request):
        form = EditForm(request.POST, instance=request.user)
        profileform = EditProfileImageForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid() and profileform.is_valid():
            form.save()
            profileform.save()
            return redirect('/account/profile')

    def get(self, request):
        form = EditForm(instance=request.user)
        profileform = EditProfileImageForm(instance=request.user.userprofile)
<<<<<<< Updated upstream
        args = {'form': form, 'profileform': profileform}

        return render(request, self.template_name, args)
=======
        return render(request, self.template_name, {'form': form, 'profileform': profileform})
>>>>>>> Stashed changes

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




