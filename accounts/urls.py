from django.conf.urls import url
from . import views
from django.contrib.auth.views import (password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete)


app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SigninFormView.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/edit/$', views.EditProfileView.as_view(), name='editprofile'),
    url(r'^profile/change-password/$', views.ChangePassword.as_view(), name='change-password'),
    url(r'^profile/reset-password/$',
        password_reset,
        {'template_name': 'registration/password_reset_form.html',
         'post_reset_redirect': 'accounts:password_reset_done'}, #it won't work without this since we are using a namespace therefore it can't find the file on its own
        name='reset_password'
        ),

    url(r'^profile/reset-password/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'
        ),

    url(r'^profile/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html',
         'post_reset_redirect': 'accounts:password_reset_complete'   # this redirects it to our custom password_reset_complete
         },
        name='password_reset_confirm'
        ),

    url(r'^profile/reset-password/complete/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'
        ),





]
