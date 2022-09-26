from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<h1>Bienvenido a su reloj</h1><br><h3><b>la fecha y hora Actual es: </b></h3>"+str(dt)+"<br><a href=https://time.is/es/Chile>Hora en Chile</a> "
    return HttpResponse(s)

def displayHola(request):
    s = '<h1><b>Inacap</b></h1><br><h2>Usted se encuentra en Inacap sede Chillan</h2><br><p><span style="color:red">INACAP</span> <b>(Instituto Nacional de Capacitación Profesional)</b> es una institución de educación superior chilena, corporación de derecho privado, fundada el 21 de octubre de 1966. INACAP distingue un subsistema técnico-profesional a través del instituto profesional INACAP y el Centro de Formación Técnica INACAP, y un subsistema universitario a través de la Universidad Tecnológica de Chile INACAP la cual tiene su cierre programado para 2030.</p>'
    return HttpResponse(s)
