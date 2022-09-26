from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def displayJuego(request):
    s = "<h1>Juegos Steam</h1><h2>Cs:Go</h2><p>El juego consiste en dos equipos, los <span style='color:red'><u>Terroristas</u></span> y los <span style='color:blue'><u>Antiterroristas</u></span> (T y CT, respectivamente), los cuales se enfrentan entre ellos en diferentes modos de juego. El modo más común es en el cual el bando Terrorista tienen que plantar y defender una bomba mientras los Antiterroristas defender las zonas de plante de la bomba y su posterior desactivación.</p>"
    return HttpResponse(s)

def displayTiempo(request):
    s = "<h1>El Tiempo</h1><p>El tiempo de hoy es: <b>Nublado</b><br><a href='https://www.meteored.cl/tiempo-en_Chillan-America+Sur-Chile-Biobio--1-18264.html'>Tiempo Aqui</a></p>"
    return HttpResponse(s)