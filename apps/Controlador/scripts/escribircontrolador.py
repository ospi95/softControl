from pymodbus.client.sync import ModbusSerialClient

class Escribircontrolador:
    def escribir(self, port, vel, id, dir, request):
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )
        client.write_register(address=dir, value=1, unit=id)