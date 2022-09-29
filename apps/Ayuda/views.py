from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
# Create your views here.


class AcercaDe(TemplateView):

    template_name = 'AcercaDe.html'


class ManualControlador(TemplateView):

    def get(self, request, *args, **kwargs):

        response = FileResponse(open('templates\Ayuda\Manual_MC5X38.pdf', 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename=Manual_MC5X38.pdf"

        return response


class ManualUsuario(TemplateView):

    def get(self, request, *args, **kwargs):

        response = FileResponse(open('templates\Ayuda\Manual_MC5X38.pdf', 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename=Manual_MC5X38.pdf"

        return response
    

class Diagrama(TemplateView):

    def get(self, request, *args, **kwargs):

        response = FileResponse(open('templates\Ayuda\PID.pdf', 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename=PID.pdf"

        return response
