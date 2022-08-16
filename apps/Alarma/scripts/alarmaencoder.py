from apps.Alarma.scripts.alarma import *

def alarmaEncoder(alarma):
    if isinstance(alarma, Alarma):
        return {
            'secuencia': alarma.secuencia,
            'fecha': alarma.fecha,
            'controlador': alarma.controlador,
            'tipo': alarma.tipo,
            'estado': alarma.estado,
            'PV': alarma.PV,
            'SV': alarma.SV
        }
