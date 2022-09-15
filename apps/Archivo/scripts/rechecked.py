def rechecked(request):
    sesion = request.session

    data = {}
    if 'EstaPV1' in sesion['EstadoGrafica']:
        data['valorPV1'] = 'checked'
    else:
        data['valorPV1'] = ''
    
    if 'EstaSV1' in sesion['EstadoGrafica']:
        data['valorSV1'] = 'checked'
    else:
        data['valorSV1'] = ''
    
    if 'EstaOUT1' in sesion['EstadoGrafica']:
        data['valorOUT1'] = 'checked'
    else:
        data['valorOUT1'] = ''
    
    if 'EstaP1' in sesion['EstadoGrafica']:
        data['valorP1'] = 'checked'
    else:
        data['valorP1'] = ''
    
    if 'EstaI1' in sesion['EstadoGrafica']:
        data['valorI1'] = 'checked'
    else:
        data['valorI1'] = ''
    
    if 'EstaD1' in sesion['EstadoGrafica']:
        data['valorD1'] = 'checked'
    else:
        data['valorD1'] = ''
    
    if 'EstaPV2' in sesion['EstadoGrafica']:
        data['valorPV2'] = 'checked'
    else:
        data['valorPV2'] = ''
    
    if 'EstaSV2' in sesion['EstadoGrafica']:
        data['valorSV2'] = 'checked'
    else:
        data['valorSV2'] = ''
    
    if 'EstaOUT2' in sesion['EstadoGrafica']:
        data['valorOUT2'] = 'checked'
    else:
        data['valorOUT2'] = ''
    
    if 'EstaP2' in sesion['EstadoGrafica']:
        data['valorP2'] = 'checked'
    else:
        data['valorP2'] = ''
    
    if 'EstaI2' in sesion['EstadoGrafica']:
        data['valorI2'] = 'checked'
    else:
        data['valorI2'] = ''
    
    if 'EstaD2' in sesion['EstadoGrafica']:
        data['valorD2'] = 'checked'
    else:
        data['valorD2'] = ''
    
    return data