from datetime import datetime
from apps.Alarma.models import Alarmas

class Alarma:
    secuencia = 0
    fecha = datetime.now().isoformat()
    controlador = 0
    tipo = ''
    estado = ''
    PV = 0
    SV = 0

    def setAlarma(self, sec, fh, ctr, tip, est, vpv, vsv):
        self.secuencia = sec
        self.fecha = fh
        self.controlador = ctr
        self.tipo = tip
        self.estado = est
        self.PV = vpv
        self.SV = vsv

    def ingresarRegistro(self):
        Alarmas(
            secuencia=self.secuencia,
            fecha=self.fecha,
            controlador=self.controlador,
            tipo=self.tipo,
            estado=self.estado,
            PV=self.PV,
            SV=self.SV
        ).save()

    def getSecuencia(self):
        return(self.secuencia)

    def getFechaHora(self):
        return(self.fecha)

    def getControlador(self):
        return(self.controlador)

    def getTipo(self):
        return(self.tipo)

    def getEstado(self):
        return(self.estado)

    def getPv(self):
        return(self.PV)

    def getSv(self):
        return(self.SV)