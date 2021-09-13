from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .data_parser import parse_ophtalmo


def index(request):
    template = loader.get_template('ophtalmo_template.html')
    context = parse_ophtalmo()
    return HttpResponse(template.render(context, request))
