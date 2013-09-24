from django.conf.urls import patterns, url

from ciip import views

urlpatterns = patterns('',
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login ,name='login')
)
