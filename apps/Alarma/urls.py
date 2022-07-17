
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from.views import *
app_name = "alarma"

urlpatterns = [
    path('home/', home.as_view(), name='home'),
]
