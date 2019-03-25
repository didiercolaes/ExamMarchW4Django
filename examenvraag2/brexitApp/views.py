# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
from datetime import date

# Create your views here.
def index (request):
    time = datetime.datetime.now() 
    ukTime = datetime.datetime(2019, 3,29, 23)
    delta = ukTime - time +1
    return render(request, 'index.html', {'time': delta})