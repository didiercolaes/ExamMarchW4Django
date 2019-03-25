from . import views
from django.conf.urls import url

app_name = 'app'

urlpatterns = [
    url('', views.index, name='index')
]