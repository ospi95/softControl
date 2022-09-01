from apps.Controlador.scripts.controladores import *

def controladoresEncoder(controles):
    if isinstance(controles, Controladores):
        return {
            'controlador1': controles.controlador1,
            'controlador2': controles.controlador2,
        }
