# app/view/producto.py
from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404, redirect #redirect necesario para trabajar con ajax
from app.models import Producto
from app.forms import ProductoForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse, JsonResponse #necesario para trabajar con json

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
    else:
        form = ProductoForm()
    return render(request, 'app/crear_producto.html', {'form': form})
       
def listar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'app/listar_producto.html', {'productos': productos})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/actualizar_producto.html', {'form': form, 'producto': producto})   

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_producto')
    return render(request, 'app/eliminar_producto.html', {'producto': producto})

def generar_lista_productos_pdf(request):
    productos = Producto.objects.all() # Obtén todos tus productos desde la base de datos
    template_path = 'app/listar_producto.html'
    context = {'productos': productos}

    # Renderiza la plantilla HTML
    template = get_template(template_path)
    html = template.render(context)

    # Crea el PDF
    response = BytesIO()
    
    #Genera el PDF
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

    if not pdf.err:
        response_pdf = HttpResponse(response.getvalue(), content_type='application/pdf')
        response_pdf['Content-Disposition'] = 'attachment; filename="lista_de_productos.pdf"'
        return response_pdf
    return HttpResponse('Tuvimos algunos errores <pre>%s</pre>' % html)
