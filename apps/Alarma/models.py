from datetime import datetime
from django.db import models

# Create your models here.

class Alarmas(models.Model):
    secuencia = models.FloatField(default=2, verbose_name='Secuencia')
    fecha = models.CharField(default=datetime.now().isoformat(), max_length=150, verbose_name='Fecha')
    controlador = models.IntegerField(default=0, verbose_name='Controlador')
    tipo = models.CharField(default='', max_length=150, verbose_name='Tipo')
    estado = models.CharField(default='', max_length=150, verbose_name='Estado')
    PV = models.FloatField(default=0, verbose_name='Process Value')
    SV = models.FloatField(default=0, verbose_name='Set Value')

    class Meta:
        verbose_name = 'Alarma'
        verbose_name_plural = 'Alarmas'
        db_table = 'Alarmas'
        ordering = ['secuencia']
