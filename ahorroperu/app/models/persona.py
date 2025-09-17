# app/models/producto.py
from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)

    class Meta:
        db_table = 'persona'
        managed = True #Django controla la tabla en la base de datos
