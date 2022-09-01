from serial.tools import list_ports

def buscarPuertos():

    allports = list_ports.comports()
    ports = []
    for p in allports:
        print(p.device)
        ports.append(p.device)

    return ports