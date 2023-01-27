import snap7
import struct

ip = "192.168.0.30"
rack=0
slot= 0 
puerto = 102

db = 1
inicio=0
tamaño=16

#Crea una instancia del cliente
client = snap7.client.Client()

#Son la ip, dos números que no son relevantes y el puerto 102 por defecto
client.connect(ip,rack,slot,puerto)

#Devuelve True si establece conexión correctamente
conexion = client.get_connected()
if conexion == True:
    print("Se ha establecido la conexión.")

    #Devuelve string del estado de la conexion
    estado = client.get_cpu_state()
    if estado == "S7CpuStatusRun":
        print("El PLC esta en marcha.")
    else:
        print("El PLC no está en marcha.")

    #Lee un bytearray con la información del DB.
    data = client.db_read(db,inicio,tamaño)

    #Escritura
    activar=True
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
else:
    print("No se puedo establecer la conexión.")
    print(f"compruebe que el PLC tiene la ip: {ip} y el puerto {puerto} abiertos.") 
