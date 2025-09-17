# app/view/producto.py
from django.shortcuts import render, redirect, get_object_or_404, redirect #redirect necesario para trabajar con ajax
from app.models import Persona
from app.forms import PersonaForm
from django.http import JsonResponse #necesario para trabajar con json

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_persona')
    else:
        form = PersonaForm()
    return render(request, 'app/crear_persona.html', {'form': form})
       
def listar_persona(request):
    personas = Persona.objects.all()
    return render(request, 'app/listar_persona.html', {'personas': personas})
   
def actualizar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_persona')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'app/actualizar_persona.html', {'form': form, 'persona': persona})   

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('listar_persona')
    return render(request, 'app/eliminar_persona.html', {'persona': persona})


