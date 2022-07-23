from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name='Home.html'

class Monitor(TemplateView):
    template_name='Softcontrol.html'