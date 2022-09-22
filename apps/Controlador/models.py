from django.db import models
from datetime import datetime

# Create your models here.


class Registros(models.Model):
    secuencia = models.IntegerField(default=None, verbose_name='Secuencia')
    fecha = models.CharField(default=datetime.now().isoformat(), max_length=200, verbose_name='Fecha')
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
        
        return 'FECHA: {} // PV1: {} // SV1: {} // OUT1: {} // P1: {} // I1: {} // D1: {} // PV2: {} // SV2: {} // OUT2: {} // P2: {} // I2: {} // D2: {}'.format(self.fecha, self.PV1, self.SV1, self.OUT1, self.P1, self.I1, self.D1, self.PV2, self.SV2, self.OUT2, self.P2, self.I2, self.D2)

    class Meta:
        verbose_name = 'Registros'
        verbose_name_plural = 'Registros'
        db_table = 'Registros'
        ordering = ['fecha']