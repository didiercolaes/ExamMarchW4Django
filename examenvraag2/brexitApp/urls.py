from . import views
from django.conf.urls import url

app_name = 'brexitApp'

urlpatterns = [
    url('', views.index, name='index')
]