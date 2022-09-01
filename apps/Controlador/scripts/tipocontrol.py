
def tipocontrol(request):
    sesion = request.session
    controlador = 0
    estado = 'disabled'
    selectedPresion = ''
    selectedFlujo = ''
    selectedCascada = ''

    if str(sesion['cascada'] == 'botonOrange'):
        selectedCascada = 'selected'
    else:
        if str(sesion['presion'] == 'NO'):
            selectedFlujo = 'selected'
        else:
            selectedPresion = 'selected'

    if sesion['controlador'] == None:
        controladro = int(sesion['controlador'])

    if controlador > 0:
        estado = 'enabled'