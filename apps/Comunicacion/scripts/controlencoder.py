from apps.Comunicacion.scripts.control import *

def controlEncoder(control):
    if isinstance(control, Control):
        return {
            'escribir': control.escribir,
            'c1': control.c1,
            'c2': control.c2,
            'aac1': control.aac1,
            'ac1': control.ac1,
            'bbc1': control.bbc1,
            'aac2': control.aac2,
            'ac2': control.ac2,
            'bbc2': control.bbc2,
            'aux1': control.aux1,
            'aux2': control.aux2,
            'histeresis': control.histeresis,
            'tipo1': control.tipo1,
            'estadoAlarmaAlta1': control.estadoAlarmaAlta1,
            'estadoAlarmaMedia1': control.estadoAlarmaMedia1,
            'estadoAlarmaBaja1': control.estadoAlarmaBaja1,
            'tipo2': control.tipo2,
            'estadoAlarmaAlta2': control.estadoAlarmaAlta2,
            'estadoAlarmaMedia2': control.estadoAlarmaMedia2,
            'estadoAlarmaBaja2': control.estadoAlarmaBaja2,
        }
