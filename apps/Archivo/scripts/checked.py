def checked(request):
    data = {}
    if 'PV1' in request.POST:
        data['EstaPV1'] = 'checked'
    
    if 'SV1' in request.POST:
        data['EstaSV1'] = 'checked'
    
    if 'OUT1' in request.POST:
        data['EstaOUT1'] = 'checked'
    
    if 'P1' in request.POST:
        data['EstaP1'] = 'checked'
    
    if 'I1' in request.POST:
        data['EstaI1'] = 'checked'
    
    if 'D1' in request.POST:
        data['EstaD1'] = 'checked'
    
    if 'PV2' in request.POST:
        data['EstaPV2'] = 'checked'
    
    if 'SV2' in request.POST:
        data['EstaSV2'] = 'checked'
    
    if 'OUT2' in request.POST:
        data['EstaOUT2'] = 'checked'
    
    if 'P2' in request.POST:
        data['EstaP2'] = 'checked'
    
    if 'I2' in request.POST:
        data['EstaI2'] = 'checked'
    
    if 'D2' in request.POST:
        data['EstaD2'] = 'checked'
    
    return data