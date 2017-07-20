from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    # ? means be greedy if 1 or more matches always use more
    # <variable>
    # . Any
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.connect_friend, name='connect_friend'),




]