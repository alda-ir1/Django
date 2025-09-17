# app/models/producto.py
from django.db import models

#Crea tu models aca
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'guzman_producto2'
        managed = True #Django controla la tabla en la base de datos
