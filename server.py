# Para instalar pip install Eel
import eel
from BD_Interac import devolverdatos, selectinfluxplc
import PLC_Connect

eel.init('web')
diccionario = {}
lista = []
print("http://localhost:8080/main.html")

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
def desde_hastapy(desde, hasta):

    selectinfluxplc(desde,hasta)

@eel.expose
def devolverdatospy():

    dataframe = devolverdatos()
    timestamp = dataframe["Timestamp"].tolist()
    numeros = dataframe["Entero"].tolist()
    return timestamp, numeros

eel.start(port=8080)


#options eel.start('index.html', mode='chrome',host = 'localhost', port = 27000, block = True, size = (ancho, alto), position = (0, 0), disable_cache = True, close_callback = close_callback, cmdline_args = ['--browser-startup-dialog','--incognito', '--no-experiments'])



