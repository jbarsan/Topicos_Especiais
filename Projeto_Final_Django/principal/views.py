from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'principal/index.html')


def documentos(request):
    return render(request, 'principal/documentos.html')


def add_alvara(request):
    return render(request, 'principal/add_alvara.html')


def add_auto(request):
    return render(request, 'principal/add_auto.html')


def add_habitese(request):
    return render(request, 'principal/add_habite_se.html')