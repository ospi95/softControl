from django.contrib import admin
from django.urls import include, path
from apps.Monitor.views import *


urlpatterns = [
    path('', Principal.as_view(), name='principal'),
    path('Monitor/', Monitor.as_view(), name='monitor')

]
