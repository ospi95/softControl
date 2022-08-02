from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


class AcercaDe(TemplateView):

    template_name = 'AcercaDe.html'


class ManualControlador(TemplateView):

    template_name = 'Manual_Contr.html'


def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'Manual_MC5X38.pdf'

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="Manual_MC5X38.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested has not found')


class ManualUsuario(TemplateView):

    template_name = 'Manual_Usu.html'
