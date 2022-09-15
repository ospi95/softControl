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

        print(self.puerto)

        client.connect()
        result = client.read_holding_registers(address=90, count=1, unit=1)
        print(result)
        sesion['estadoPuerto'] = 'Abierto'

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