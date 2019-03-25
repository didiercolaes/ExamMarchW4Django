# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import datetime
from datetime import date

# Create your views here.
def index (request):
    time = datetime.datetime.now() 
    return render(request, 'index.html', {'time': time})