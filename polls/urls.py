from .views import index

from django.conf.urls import url
from . import views

urlpatterns=[
    url('show/',views.index),
    url('question/',views.QuetionView.as_view())


]