import snap7
import struct
from snap7.util import *

numero = 3

def lectura():

    ip = "192.168.0.30"
    rack = 0
    slot = 0
    puerto = 102

    db = 4
    inicio = 0
    tamaño = 11

    #Crea una instancia del cliente
    client = snap7.client.Client()

    #Son la ip, dos números que no son relevantes y el puerto 102 por defecto
    client.connect(ip, rack, slot, puerto)

    #Lectura
    data = client.db_read(db, inicio, tamaño)

    #Interpretar el bytearray
    #Para intepretar valores reales
    valorIntro = struct.unpack('>f', data[0:4])
    valorIntro = float(valorIntro[0])
    print(valorIntro)

    #Interpretar el bytearray
    #Para intepretar valores reales
    contador1 = struct.unpack('>f', data[4:8])
    contador1 = float(contador1[0])
    print(contador1)

    #Para interpretar valores enteros
    contador2 = int.from_bytes(data[8:10], byteorder='big')
    print(contador2)

    #Para interpretar booleanos
    salida = snap7.util.get_bool(data,10,2)
    salidaNegada = snap7.util.get_bool(data, 10, 1)
    print(salida)
    print(salidaNegada)

    #Desconectar
    client.disconnect()

def datos():
        ip = "192.168.0.30"
        rack = 0
        slot = 0 
        puerto = 102

        db = 1
        inicio =0
        tamaño =16

        #Crea una instancia del cliente
        client = snap7.client.Client()

        #Son la ip, dos números que no son relevantes y el puerto 102 por defecto
        client.connect(ip,rack,slot,puerto)

        #Devuelve True si establece conexión correctamente
        print("Se ha establecido la conexión.")

        #Devuelve string del estado de la conexion
        estado = client.get_cpu_state()
        if estado == "S7CpuStatusRun":
            print("El PLC esta en marcha.")
        else:
            print("El PLC no está en marcha.")

        #Lee un bytearray con la información del DB.
        data = client.db_read(db,inicio,tamaño)

        #Variables para la escritura
        activar=False
        input=70.5

        #Para escribir un booleano
        snap7.util.set_bool(data, 6, 1, activar)
            
        #Para escribir un float
        snap7.util.set_real(data,8,input)

        #Reintroduces al completo
        client.db_write(db, inicio, data)

        #Interpretar el bytearray
        #Para intepretar valores reales
        contador1 = struct.unpack('>f',data[0:4])
        contador1=float(contador1[0])
        print(contador1)

        #Para interpretar valores enteros
        contador2=int.from_bytes(data[4:6],byteorder='big')
        print(contador2)

        #Para interpretar booleanos
        salida=bool(data[6])
        print(salida)

        #Leer output
        output = struct.unpack('>f', data[8:12])
        output = float(output[0])
        print(output)
        client.disconnect()

def escritura():
    ip = "192.168.0.30"
    rack = 0
    slot = 0
    puerto = 102

    db = 5
    inicio = 0
    tamaño = 5

    #Crea una instancia del cliente
    client = snap7.client.Client()

    #Son la ip, dos números que no son relevantes y el puerto 102 por defecto
    client.connect(ip, rack, slot, puerto)


    #Lee un bytearray con la información del DB.
    data = client.db_read(db, inicio, tamaño)

    #Variables para la escritura
    activar = False
    input = 70.5

    #Para escribir un float
    snap7.util.set_real(data, 0, input)

    #Para escribir un booleano
    snap7.util.set_bool(data, 4, 0, activar)
  
    #Reintroduces al completo
    client.db_write(db, inicio, data)

    client.disconnect()




if numero == 1:
    datos()
if numero == 2:
    lectura()
if numero == 3:
    escritura()
    lectura()
    

