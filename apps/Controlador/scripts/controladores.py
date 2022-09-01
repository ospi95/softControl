class Controladores:
    controlador1 = 999
    controlador2 = 999

    def setRegistro(self, c1, c2):
        controlador1 = c1
        controlador2 = c2

    def setControlador1(self, c1):
        controlador1 = c1

    def setControlador2(self, c2):
        controlador2 = c2

    def getControlador1(self):
        return self.controlador1

    def getControlador2(self):
        return self.controlador2