from django.db import models
from datetime import datetime

# Create your models here.


class Registro(models.Model):
    secuencia = models.IntegerField(default=None, verbose_name='Secuencia')
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    PV1 = models.FloatField(default=None, verbose_name='Process Value 1')
    SV1 = models.FloatField(default=None, verbose_name='Set Value 1')
    OUT1 = models.FloatField(default=None, verbose_name='Salida 1')
    P1 = models.FloatField(default=None, verbose_name='Valor Proporcional 1')
    I1 = models.FloatField(default=None, verbose_name='Valor Integral 1')
    D1 = models.FloatField(default=None, verbose_name='Valor Derivativo 1')
    PV2 = models.FloatField(default=None, verbose_name='Process Value 2')
    SV2 = models.FloatField(default=None, verbose_name='Set Value 2')
    OUT2 = models.FloatField(default=None, verbose_name='Salida 2')
    P2 = models.FloatField(default=None, verbose_name='Valor Proporcional 2')
    I2 = models.FloatField(default=None, verbose_name='Valor Integral 2')
    D2 = models.FloatField(default=None, verbose_name='Valor Derivativo 2')

    def __str__(self):
        return str(self.secuencia)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        db_table = 'Registro'
        ordering = ['secuencia']