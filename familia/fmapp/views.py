import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from fmapp.models import familia


def lista_familia(requets):
    queryset = familia.objects.all()

    diccionario = {'fmapp': queryset}

    plantilla = loader.get_template('template1.html')

    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)