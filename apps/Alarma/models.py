from datetime import datetime
from django.db import models

# Create your models here.


class Alarmas(models.Model):
    secuencia = models.FloatField(default=None, verbose_name='Secuencia')
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    controlador = models.IntegerField(default=None, verbose_name='Controlador')
    tipo = models.CharField(max_length=150, verbose_name='Tipo')
    estado = models.CharField(max_length=150, verbose_name='Estado')
    PV = models.FloatField(default=None, verbose_name='Process Value')
    SV = models.FloatField(default=None, verbose_name='Set Value')

    def __str__(self):
        return str(self.secuencia)

    class Meta:
        verbose_name = 'Alarma'
        verbose_name_plural = 'Alarmas'
        db_table = 'Alarmas'
        ordering = ['secuencia']
