import math
from pymodbus.client.sync import ModbusSerialClient

def lecturamonitor(port, vel):

    client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )

    client.connect()
    #LECTURA CONTROLADOR 1
    #Lectura del controlador (Numero decimales para PV y SV)
    result = client.read_holding_registers(address=83, count=1, unit=1)
    d = int(math.pow(10, result.registers[0]))
    
    #Lectura del controlador (SV, OUT)
    result = client.read_holding_registers(address=2, count=2, unit=1)
    sv1 = result.registers[0]
    out1 = result.registers[1]
    if sv1 > 63000:
        sv1 = sv1 - 65536
    sv1 = sv1/d
    out1 = out1/10
    
    #Lectura del controlador (PV)
    result = client.read_holding_registers(address=256, count=1, unit=1)
    pv1 = result.registers[0]
    if pv1 > 63000:
        pv1 = pv1 - 65536
    pv1 = pv1/d
    
    # LECTURA CONTROLADOR 2
    # Lectura del controlador (Numero decimales para PV y SV)
    result = client.read_holding_registers(address=83, count=1, unit=2)
    d = int(math.pow(10, result.registers[0]))
    
    # Lectura del controlador (SV, OUT)
    result = client.read_holding_registers(address=2, count=2, unit=2)
    sv2 = result.registers[0]
    out2 = result.registers[1]
    if sv2 > 63000:
        sv2 = sv2 - 65536
    sv2 = sv2/d
    out2 = out2/10

    # Lectura del controlador (PV)
    result = client.read_holding_registers(address=256, count=1, unit=2)
    pv2 = result.registers[0]
    if pv2 > 63000:
        pv2 = pv2 - 65536
    pv2 = pv2 / d

    client.close()

    return [pv1, sv1, out1, pv2, sv2, out2]