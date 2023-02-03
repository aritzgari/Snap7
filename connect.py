import snap7
import struct
from snap7.util import *

def lectura():

    ip = "192.168.0.30"
    rack = 0
    slot = 0
    puerto = 102

    db = 4
    inicio = 0
    tamaño = 11

    lista = []
    # Crea una instancia del cliente
    client = snap7.client.Client()

    # Son la ip, dos números que no son relevantes y el puerto 102 por defecto
    client.connect(ip, rack, slot, puerto)

    # Lectura
    data = client.db_read(db, inicio, tamaño)

    # Interpretar el bytearray
    # Para intepretar valores reales
    valorIntro = struct.unpack('>f', data[0:4])
    valorIntro = float(valorIntro[0])

    # Interpretar el bytearray
    # Para intepretar valores reales
    contador1 = struct.unpack('>f', data[4:8])
    contador1 = float(contador1[0])

    # Para interpretar valores enteros
    contador2 = int.from_bytes(data[8:10], byteorder='big')

    # Para interpretar booleanos
    salida = snap7.util.get_bool(data, 10, 0)

    lista = [salida, contador1, contador2, valorIntro]

    # Desconectar
    client.disconnect()

    
    return lista

def botonsalida(activar):
    ip = "192.168.0.30"
    rack = 0
    slot = 0
    puerto = 102

    db = 5
    inicio = 4
    tamaño = 1

    # Crea una instancia del cliente
    client = snap7.client.Client()

    # Son la ip, dos números que no son relevantes y el puerto 102 por defecto
    client.connect(ip, rack, slot, puerto)

    # Lee un bytearray con la información del DB.
    data = client.db_read(db, inicio, tamaño)

    # Para escribir un booleano
    snap7.util.set_bool(data, 0, 0, activar)

    # Reintroduces al completo
    client.db_write(db, inicio, data)

    client.disconnect()

def input(velocidad):
    ip = "192.168.0.30"
    rack = 0
    slot = 0
    puerto = 102

    db = 5
    inicio = 0
    tamaño = 4

    # Crea una instancia del cliente
    client = snap7.client.Client()

    # Son la ip, dos números que no son relevantes y el puerto 102 por defecto
    client.connect(ip, rack, slot, puerto)

    # Lee un bytearray con la información del DB.
    data = client.db_read(db, inicio, tamaño)

    # Para escribir un float
    snap7.util.set_real(data, 0, velocidad)

    # Reintroduces al completo
    client.db_write(db, inicio, data)

    client.disconnect()
