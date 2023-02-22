# Para instalar pip install Eel

import eel
from BD_Interac import selectinfluxplc
import PLC_Connect




eel.init('web')
diccionario = {}
lista = []

# Permite activar una salida del plc usando Snap7
@eel.expose
def activarpy():
    PLC_Connect.botonsalida(True)

# Permite desactivar una salidad del plc usando Snap7
@eel.expose
def desactivarpy():
    PLC_Connect.botonsalida(False)

#Este apartado te permite escribir variables reales en PLC
@eel.expose
def inputdatos(velocidad):

    PLC_Connect.input(float(velocidad))

#Este apartado te permite tomar datos del PLC usando Snap7
@eel.expose
def datospy():

    lista = PLC_Connect.lectura()

    return lista

#Para el desde hasta
@eel.expose
def desde_hasta(desde, hasta):
    #Para hacer pruebas
    #print(desde,hasta)

    #El plot del dataframe de la simulación.
    datos=selectinfluxplc(desde,hasta)
    if datos.empty:
        print('DataFrame is empty!')
    else:
        return datos
    

eel.start('main.html', size=(800, 440), port=8080)

#options eel.start('index.html', mode='chrome',host = 'localhost', port = 27000, block = True, size = (ancho, alto), position = (0, 0), disable_cache = True, close_callback = close_callback, cmdline_args = ['--browser-startup-dialog','--incognito', '--no-experiments'])



