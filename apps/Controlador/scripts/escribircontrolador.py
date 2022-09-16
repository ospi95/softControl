from pymodbus.client.sync import ModbusSerialClient

class Escribircontrolador:

    def escribir(self, port, vel, id, dir, valor):
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )
        client.connect()
        client.write_register(address=dir, value=valor, unit=id)
        client.close()