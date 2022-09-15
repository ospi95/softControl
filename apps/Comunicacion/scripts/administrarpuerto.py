from pymodbus.client.sync import ModbusSerialClient

class AdministrarPuerto:

    puerto = 'COM3'
    velocidad = 9600

    def abrirPuerto(self, port, vel, request):
        sesion = request.session
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )

        if client.connect():
            sesion['estadoPuerto'] = 'Abierto'
        else:
            sesion['estadoPuerto'] = 'Cerrado'

    def cerrarPuerto(self, request):
        sesion = request.session
        client = ModbusSerialClient(
            method="rtu",
            port=self.puerto,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=self.velocidad
        )
        client.close()
        sesion['estadoPuerto'] = 'Cerrado'