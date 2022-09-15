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
        connection=client.connect()
        
        if connection:
            sesion['estadoPuerto'] = 'Abierto'
        else:
            sesion['estadoPuerto'] = 'Cerrado'
        print("Entró - Abrir Puerto. ")

        client.close()
        
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
               
        client.connect()
        client.close()
        print("Entró - Cerrar Puerto. ")
        sesion['estadoPuerto'] = 'Cerrado'