# app/view/producto.py
from django.shortcuts import render, redirect, get_object_or_404, redirect #redirect necesario para trabajar con ajax
from app.models import Objeto
from app.forms import ObjetoForm
from django.http import JsonResponse #necesario para trabajar con json

def crear_objeto(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_objeto')
    else:
        form = ObjetoForm()
    return render(request, 'app/crear_objeto.html', {'form': form})
       
def listar_objeto(request):
    objetos = Objeto.objects.all()
    return render(request, 'app/listar_objeto.html', {'objetos': objetos})
   
#    Si es GET, muestra la lista de productos
#    productos = Producto.objects.all()
#    form = ObjetoForm()
#    return render(request, 'app/listar_objeto.html', {'productos': productos, 'form': form})

def actualizar_objeto(request, id):
    objeto = get_object_or_404(Objeto, id=id)
    if request.method == 'POST':
        form = ObjetoForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect('listar_objeto')
    else:
        form = ObjetoForm(instance=objeto)
    return render(request, 'app/actualizar_objeto.html', {'form': form, 'objeto': objeto})   

def eliminar_objeto(request, id):
    objeto = get_object_or_404(Objeto, id=id)
    if request.method == 'POST':
        objeto.delete()
        return redirect('listar_objeto')
    return render(request, 'app/eliminar_objeto.html', {'objeto': objeto})