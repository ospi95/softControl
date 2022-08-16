from datetime import datetime

class Registro():
    secuencia = 0
    fecha = datetime.now().isoformat()
    PV1 = 0
    SV1 = 0
    OUT1 = 0
    P1 = 0
    I1 = 0
    D1 = 0
    PV2 = 0
    SV2 = 0
    OUT2 = 0
    P2 = 0
    I2 = 0
    D2 = 0

    def setRegistro(self, sec, fh, vpv1, vsv1, vout1, vp1, vi1, vd1, vpv2, vsv2, vout2, vp2, vi2, vd2):
        secuencia = sec
        fecha = fh
        PV1 = vpv1
        SV1 = vsv1
        OUT1 = vout1
        P1 = vp1
        I1 = vi1
        D1 = vd1
        PV2 = vpv2
        SV2 = vsv2
        OUT2 = vout2
        P2 = vp2
        I2 = vi2
        D2 = vd2

    def getSecuencia(self):
        return(self.secuencia)

    def getFechaHora(self):
        return(self.fecha)

    def getPV1(self):
        return(self.PV1)

    def getSV1(self):
        return(self.SV1)

    def getOUT1(self):
        return(self.OUT1)

    def getP1(self):
        return(self.P1)

    def getI1(self):
        return(self.I1)

    def getD1(self):
        return(self.D1)

    def getPV2(self):
        return(self.PV2)

    def getSV2(self):
        return(self.SV2)

    def getOUT2(self):
        return(self.OUT2)

    def getP2(self):
        return(self.P2)

    def getI2(self):
        return(self.I2)

    def getD2(self):
        return(self.D2)