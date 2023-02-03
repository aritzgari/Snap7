# Para instalar pip install Eel
import paho.mqtt.client as mqtt
import eel
import connect

eel.init('web')

diccionario = {}
lista = []

# Permite activar una salida del plc
@eel.expose
def activarpy():
    connect.botonsalida(True)

# Permite desactivar salidas del plc
@eel.expose
def desactivarpy():
    connect.botonsalida(False)

# Este apartado te permite tomar datos del PLC
@eel.expose
def datospy():

    lista=connect.lectura()

    return lista

#Este apartado te permite escribir variables reales en PLC
@eel.expose
def inputdatos(velocidad):

    connect.input(float(velocidad))


eel.start('main.html', size=(800, 420)) 

#options eel.start('index.html', mode='chrome',host = 'localhost', port = 27000, block = True, size = (700, 480), position = (0, 0), disable_cache = True, close_callback = close_callback, cmdline_args = ['--browser-startup-dialog','--incognito', '--no-experiments'])
#size(ancho,alto)



