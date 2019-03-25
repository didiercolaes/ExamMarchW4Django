from . import views
from django.conf.urls import url
from django.urls import path, include

app_name = 'brexitApp'

urlpatterns = [
    path('', views.index, name='index')
]