from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

# Create your views here.
def index(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
    )
    


def disciplina(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'disciplina.html',
    )
    

def cursos(request):
    """Renders the contact page."""
    return render(
        request,
        'lstcursos.html',

    )

    
def noticias(request):
    """Renders the contact page."""
    return render(
        request,
        'noticias.html',

    )
