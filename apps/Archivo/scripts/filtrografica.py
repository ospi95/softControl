from apps.Controlador.models import Registros
from datetime import datetime

def filtrografica(request, start_date, end_date):
    sesion = request.session
    date = []
    pv1 = []
    sv1 = []
    out1 = []
    p1 = []
    i1 = []
    d1 = []
    pv2 = []
    sv2 = []
    out2 = []
    p2 = []
    i2 = []
    d2 = []

    search = Registros.objects.filter(fecha__range=(start_date, end_date))

    for s in search:
        date.append(datetime.fromisoformat(s.fecha).timestamp()*1000)
        pv1.append(s.PV1)
        sv1.append(s.SV1)
        out1.append(s.OUT1)
        p1.append(s.P1)
        i1.append(s.I1)
        d1.append(s.D1)
        pv2.append(s.PV2)
        sv2.append(s.SV2)
        out2.append(s.OUT2)
        p2.append(s.P2)
        i2.append(s.I2)
        d2.append(s.D2)
    
    data = {}
    data['date'] = date
    
    if 'EstaPV1' in sesion['EstadoGrafica']:
        data['PV1'] = pv1
    else:
        data['PV1'] = []
    
    if 'EstaSV1' in sesion['EstadoGrafica']:
        data['SV1'] = sv1
    else:
        data['SV1'] = []
    
    if 'EstaOUT1' in sesion['EstadoGrafica']:
        data['OUT1'] = out1
    else:
         data['OUT1'] = []
    
    if 'EstaP1' in sesion['EstadoGrafica']:
        data['P1'] = p1
    else:
        data['P1'] = []
    
    if 'EstaI1' in sesion['EstadoGrafica']:
        data['I1'] = i1
    else:
        data['I1'] = []
    
    if 'EstaD1' in sesion['EstadoGrafica']:
        data['D1'] = d1
    else:
        data['D1'] = []
    
    if 'EstaPV2' in sesion['EstadoGrafica']:
        data['PV2'] = pv2
    else:
        data['PV2'] = []
    
    if 'EstaSV2' in sesion['EstadoGrafica']:
        data['SV2'] = sv2
    else:
        data['SV2'] = []
    
    if 'EstaOUT2' in sesion['EstadoGrafica']:
        data['OUT2'] = out2
    else:
        data['OUT2'] = []
    
    if 'EstaP2' in sesion['EstadoGrafica']:
        data['P2'] = p2
    else:
        data['P2'] = []
    
    if 'EstaI2' in sesion['EstadoGrafica']:
        data['I2'] = i2
    else:
        data['I2'] = []
    
    if 'EstaD2' in sesion['EstadoGrafica']:
        data['D2'] = d2
    else:
        data['D2'] = []
    
    return data
    
    

        