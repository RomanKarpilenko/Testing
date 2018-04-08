from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^1', views.index1, name='index1'),
    url(r'^', views.index, name='index')
]
