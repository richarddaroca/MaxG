import re

from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

# https://www.youtube.com/watch?v=DbAzWll4UIA&index=27&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]  # This exempts the the login page # the lstip removes the '/' on the string
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):                  # This checks if settings.py has the LOGIN_EXEMPT_URLS attribute
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]  # This adds all the regex in LOGIN_EXEMPT_URLS to EXEMPT_URLS

class LoginRequiredMiddleware:

    def __init__(self, get_response):               # this is required for middelware
        self.get_response = get_response

# https://www.youtube.com/watch?v=BtxnjcVl68M&index=26&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj

    def __call__(self, request):                      # this fixes the errorr instance has no __call__ method
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):     # the process view method will run when django is about to call a view function
        assert hasattr(request, 'user')                # This checks if the user attribute exist in our request
        path = request.path_info.lstrip('/')   # path defined as the url the user is currently trying to access
        print path



        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('accounts:logout').lstrip('/'):      # Reverse is used to generate the URL its return value will be account/logout/
            logout(request)

        if request.user.is_authenticated() and url_is_exempt:       # They are loggedin
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated() or url_is_exempt:
            return None                                            # The user is not redirected since they are login

        else:
            return redirect(settings.LOGIN_URL)





























