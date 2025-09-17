# app/models/producto.py
from django.db import models

class Objeto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'objeto'
        managed = True #Django controla la tabla en la base de datos

