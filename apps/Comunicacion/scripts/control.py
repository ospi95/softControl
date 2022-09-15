from apps.Controlador.scripts.escribircontrolador import *
from apps.Controlador.scripts.registro import *
from apps.Alarma.scripts.alarma import *
from apps.Controlador.scripts.leercontrolador import *
from apps.Controlador.scripts.registroenconder import *
import json


class Control:
    datoF = Registro()
    lc = Leercontrolador()
    escribir = False
    c1 = 0
    c2 = 0
    aac1 = 0
    ac1 = 0
    aac2 = 0
    ac2 = 0
    bbc2 = 0
    aux1 = 0
    aux2 = 0
    histeresis = 0
    tipo1 = ''
    estadoAlarmaAlta1 = ''
    estadoAlarmaMedia1 = ''
    estadoAlarmaBaja1 = ''
    tipo2 = ''
    estadoAlarmaAlta2 = ''
    estadoAlarmaMedia2 = ''
    estadoAlarmaBaja2 = ''

    @staticmethod
    def read(puerto, vel, id1, id2, request):
        sesion = request.session
        sesion['threadRead'] = 1

        def run():
            while int(sesion['threadRead']) == 1:
                lc = Leercontrolador()
                if id1 != 999:
                    aux1 = lc.leerDireccion(puerto, vel, id1, 5)

                    if id1 == 99999:
                        sesion['manual1'] = 'botonBlack'
                    elif id1 == 0:
                        sesion['manual1'] = 'botonBlack'
                    elif id1 == 1:
                        sesion['manual1'] = 'botonYellow'
                    elif id1 == 2:
                        sesion['manual1'] = 'botonYellow'

                if id2 != 999:
                    aux1 = lc.leerDireccion(puerto, vel, id1, 5)
                    if id2 == 99999:\
                        sesion['manual2'] = 'botonBlack'
                    elif id2 == 0:
                        sesion['manual2'] = 'botonBlack'
                    elif id2 == 1:
                        sesion['manual2'] = 'botonYellow'
                    elif id2 == 2:
                        sesion['manual2'] = 'botonYellow'

                datoF = lc.leer(puerto, vel, id1, id2)
                sesion['dato'] = json.dumps(datoF, default=registroEncoder)

                if sesion['cascada'] == 'botonOrange':
                    aux1 = lc.leerDireccion(puerto, vel, id2, 76)
                    aux2 = lc.leerDireccion(puerto, vel, id2, 77)
                    aux2 = (((aux2-aux1)*datoF.getOUT1())/100)+aux1
                    ec = Escribircontrolador()
                    ec.escribir(puerto, vel, id2, 2, int(aux2))

                if int(sesion['threadRead']) == 1:
                    sesion['salvando'] = 'En lectura...'

                sesion['threadRead'] = 0
            sesion['hiloParado'] = 1

        run()

    @staticmethod
    def write(puerto, vel, id1, id2, request):
        sesion = request.session

        sesion['threadWrite'] = 1
        sesion['hiloParado'] = 0

        def run():
            while int(sesion['threadWrite']) == 1:
                lc = Leercontrolador()
                if id1 != 999:
                    aux1 = lc.leerDireccion(puerto, vel, id1, 5)
                    print('falta configurar Leer Direccion')
                    if aux1 == 0:
                        sesion['manual1'] = 'botonBlack'
                    else:
                        sesion['manual1'] = 'botonYellow'

                if id2 != 999:
                    aux1 = lc.leerDireccion(puerto, vel, id1, 5)
                    print('falta configurar Leer Direccion')
                    if aux1 == 0:
                        sesion['manual2'] = 'botonBlack'
                    else:
                        sesion['manual2'] = 'botonYellow'

                datoF = lc.leer(puerto, vel, id1, id2)
                sesion['dato'] = json.dumps(datoF, default=registroEncoder)
                sesion['dato'] = datoF

                if sesion['cascada'] == 'botonOrange':
                    aux1 = lc.leerDireccion(puerto, vel, id2, 76)
                    aux2 = lc.leerDireccion(puerto, vel, id2, 77)
                    aux2 = (((aux2 - aux1) * datoF.getOUT1()) / 100) + aux1
                    ec = Escribircontrolador()
                    ec.escribir(puerto, vel , id2, 2 , int(aux2))

                if int(sesion['threadWrite']) == 1:
                    sesion['salvando'] = 'En lectura...'

                if int(sesion['threadWrite']) == 1:
                    sesion['salvando'] = 'Salvando...'

            sesion['hiloParado'] = 1

        run()

    @staticmethod
    def events(request):
        sesion = request.session
        sesion['threadEvents'] = 1

        def run():
            alarma = Alarma()
            while int(sesion['threadEvents']) == 1:
                if str(sesion['alarmaHabilitada']) == 'enabled':
                    escribir = False
                    try:
                        c1 = int(sesion['controlador1'])
                        c2 = int(sesion['controlador2'])
                        histeresis = float(sesion['histeresis'])
                        datoF = json.load(sesion['dato'])
                        if (c1 == 1) and (float(datoF['PV1']) != -99999):
                            aac1 = float(sesion['alta1'])
                            ac1 = float(sesion['media1'])
                            bbc1 = float(sesion['baja1'])
                            estadoAlarmaAlta1 = str(sesion['estadoAlarmaAlta1'])
                            estadoAlarmaMedia1 = str(sesion['estadoAlarmaMedia1'])
                            estadoAlarmaBaja1 = str(sesion['estadoAlarmaBaja1'])
                            if (float(datoF['PV1']) > aac1) and (estadoAlarmaAlta1 == 'Inactiva'):
                                sesion['estadoAlarma1'] = 'Activa'
                                sesion['alarma1'] = 'botonRed'
                                alarma.setAlarma(0, str(datoF['fecha']), 1, 'Alta-Alta', 'Activa', float(datoF['PV1']), float(datoF['SV1']))
                                escribir = True
                            if (float(datoF['PV1']) <= (aac1-(histeresis*aac1/100))) and estadoAlarmaAlta1 == 'Inactiva':
                                sesion['estadoAlarmaAlta1'] = 'Inactiva'
                                sesion['alarma1'] = 'botonBlack'
                                alarma.setAlarma(0, str(datoF['fecha']), 1, 'Alta-Alta', 'Inactiva', float(datoF['PV1']), float(datoF['SV1']))
                                escribir = True
                            if (float(datoF['PV1']) > ac1) and (estadoAlarmaMedia1 == 'Inactiva'):
                                sesion['estadoAlarmaMedia1'] = 'Activa'
                                sesion['alarma1'] = 'botonRed'
                                alarma.setAlarma(0, str(datoF['fecha']), 1, 'Alta', 'Activa', float(datoF['PV1']), float(datoF['SV1']))
                                escribir = True
                            if (float(datoF['PV1']) <= (ac1-(histeresis*ac1/100))) and (estadoAlarmaMedia1 == 'Inactiva'):
                                sesion['estadoAlarmaMedia1'] = 'Inactiva'
                                sesion['alarma1'] = 'botonBlack'
                                alarma.setAlarma(0, str(datoF['fecha']), 1, 'Alta', 'Inactiva', float(datoF['PV1']), float(datoF['SV1']))
                                escribir = True
                            if (float(datoF['PV1']) < bbc1) and (estadoAlarmaBaja1 == 'Inactiva'):
                                sesion['estadoAlarmaBaja1'] = 'Activa'
                                sesion['alarma1'] = 'botonRed'
                                alarma.setAlarma(0, str(datoF['fecha']), 1, 'Baja-Baja', 'Activa', float(datoF['PV1']), float(datoF['SV1']))
                                escribir = True
                            if (float(datoF['PV1']) >= (bbc1-(histeresis*bbc1/100))) and (estadoAlarmaBaja1 == 'Inactiva'):
                                sesion['estadoAlarmaBaja1'] = 'Inactiva'
                                sesion['alarma1'] = 'botonBlack'
                                alarma.setAlarma(0, str(datoF['fecha']), 1, 'Baja-Baja', 'Inactiva', float(datoF['PV1']), float(datoF['SV1']))
                                escribir = True
                        try:
                            if escribir:
                                alarma.ingresarRegistro()
                        finally:
                            pass

                        escribir = False
                        if (c2 == 2) and (float(datoF['PV2']) != -99999):
                            aac2 = float(sesion['alta2'])
                            ac2 = float(sesion['media2'])
                            bbc2 = float(sesion['baja2'])
                            estadoAlarmaAlta2 = str(sesion['estadoAlarmaAlta2'])
                            estadoAlarmaMedia2 = str(sesion['estadoAlarmaMedia2'])
                            estadoAlarmaBaja2 = str(sesion['estadoAlarmaBaja2'])
                            if (float(datoF['PV2']) > aac2) and (estadoAlarmaAlta2 == 'Inactiva'):
                                sesion['estadoAlarma2'] = 'Activa'
                                sesion['alarma2'] = 'botonRed'
                                alarma.setAlarma(0, str(datoF['fecha']), 2, 'Alta-Alta', 'Activa', float(datoF['PV2']), float(datoF['SV2']))
                                escribir = True
                            if (float(datoF['PV2']) <= (aac2 - (histeresis * aac2 / 100))) and estadoAlarmaAlta2 == 'Inactiva':
                                sesion['estadoAlarmaAlta2'] = 'Inactiva'
                                sesion['alarma2'] = 'botonBlack'
                                alarma.setAlarma(0, str(datoF['fecha']), 2, 'Alta-Alta', 'Inactiva', float(datoF['PV2']), float(datoF['SV2']))
                                escribir = True
                            if (float(datoF['PV2']) > ac2) and (estadoAlarmaMedia2 == 'Inactiva'):
                                sesion['estadoAlarmaMedia2'] = 'Activa'
                                sesion['alarma2'] = 'botonRed'
                                alarma.setAlarma(0, str(datoF['fecha']), 2, 'Alta', 'Activa', float(datoF['PV2']), float(datoF['SV2']))
                                escribir = True
                            if (float(datoF['PV2']) <= (ac2 - (histeresis * ac2 / 100))) and (estadoAlarmaMedia2 == 'Inactiva'):
                                sesion['estadoAlarmaMedia2'] = 'Inactiva'
                                sesion['alarma2'] = 'botonBlack'
                                alarma.setAlarma(0, str(datoF['fecha']), 2, 'Alta', 'Inactiva', float(datoF['PV2']), float(datoF['SV2']))
                                escribir = True
                            if (float(datoF['PV2']) < bbc2) and (estadoAlarmaBaja2 == 'Inactiva'):
                                sesion['estadoAlarmaBaja2'] = 'Activa'
                                sesion['alarma2'] = 'botonRed'
                                alarma.setAlarma(0, str(datoF['fecha']), 2, 'Baja-Baja', 'Activa', float(datoF['PV2']), float(datoF['SV2']))
                                escribir = True
                            if (float(datoF['PV2']) >= (bbc2 - (histeresis * bbc2 / 100))) and (estadoAlarmaBaja2 == 'Inactiva'):
                                sesion['estadoAlarmaBaja2'] = 'Inactiva'
                                sesion['alarma2'] = 'botonBlack'
                                alarma.setAlarma(0, str(datoF['fecha']), 2, 'Baja-Baja', 'Inactiva', float(datoF['PV2']), float(datoF['SV2']))
                                escribir = True

                        try:
                            if escribir:
                                alarma.ingresarRegistro()
                        finally:
                            pass
                    finally:
                        pass
        run()
