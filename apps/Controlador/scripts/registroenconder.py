from apps.Controlador.scripts.registro import *

def registroEncoder(registro):
    if isinstance(registro, Registro):
        return {
            'fecha': registro.fecha,
            'PV1': registro.PV1,
            'SV1': registro.SV1,
            'OUT1': registro.OUT1,
            'P1': registro.P1,
            'I1': registro.I1,
            'D1': registro.D1,
            'PV2': registro.PV2,
            'SV2': registro.SV2,
            'OUT2': registro.OUT2,
            'P2': registro.P2,
            'I2': registro.I2,
            'D2': registro.D2,
        }
