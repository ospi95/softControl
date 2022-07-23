from django.contrib import admin
from django.urls import include, path
from apps.Monitor.views import *


urlpatterns = [
    path('', Monitor.as_view(), name='monitor'),

]
