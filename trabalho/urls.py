# views.py
from django.urls import path
from django.contrib import admin
from core.views import *

urlpatterns = [
    path('', index),
	path('login/', login),
	path('contato/', contato),
    path('admin/', admin.site.urls)
]
