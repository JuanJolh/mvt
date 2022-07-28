from django.shortcuts import render
from familia.models import familiares

def agregar_familia(request):
    new_familiar = familiares.objects.create(name='Vicenta', apellido='Hernandez', edad='48', fecha='1994-03-10')
    context = {
        'new_familiar':new_familiar
    }
    return render(request, 'new_familiar.html', context=context)

def plantilla(request):
    return render(request, 'plantilla.html', context={})

def lista_familiares(request):
    Familiares = familiares.objects.all()
    context = {
        'Familiares':Familiares
    }
    return render(request, 'familia_lista.html', context=context)