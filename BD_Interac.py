import time
from influxdb import InfluxDBClient
from datetime import datetime, timedelta
import pandas as pd

#Seleccionar datos de Base de datos de influxDB.
def selectinfluxplc(desde, hasta):
   # Para comparar más adelante.
    today = datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    today = pd.to_datetime(today)
    mañana = pd.to_datetime(today) + timedelta(days=1)

    # Se le añade un día por que sino va al día correcto pero hasta el inicio del día y no muestra lo del día (hasta 00:00:00)
    hasta = pd.to_datetime(hasta) + timedelta(days=1)

    # Hay que cambiar el formato para poder hacer las comparaciones
    desde = pd.to_datetime(desde)
    
    # Adaptación de fechas para que no sean imposibles.
    if desde >= today:
        hasta = mañana
        desde = today
    if desde == hasta and desde != today:
        hasta = pd.to_datetime(hasta) + timedelta(days=1)

    # Pasar de datetime a unix

    desde = int(time.mktime(desde.timetuple()) * 1000000000)
    hasta = int(time.mktime(hasta.timetuple()) * 1000000000)

    # generar el cliente de influx.
    client = InfluxDBClient(host='localhost', port=8086)

    # Seleccionar la base de datos concreta que tiene la información.
    client.switch_database('plc')

    # Hacer la query para seleccionar todo lo de la base de datos.
    result = client.query(
        f'SELECT * FROM "plc" where time > {desde} and time < {hasta}')

    # Coger solo los datos de medida de la base de datos.
    points = list(result.get_points(measurement='plc'))

    #Cerrar conexión con BD
    client.close()

    # Generar un dataframe del diccionario generado en la línea anterior.
    df = pd.DataFrame.from_dict(points)
    if df.empty:
        print('DataFrame is empty!')
    else:
        # Renombrar la columna de time para que sea compatible con el resto de funciones más adelante.
        df.rename(columns={'time': 'Timestamp'}, inplace=True)

        # Cambiar el formato de horas a uno que no tenga en cuenta la zona horaria.
        df['Timestamp'] = pd.to_datetime(df['Timestamp']).dt.tz_localize(None)

        # Cambiar el formato de datetime a string para mostrarlo más facil.
        df['Timestamp'] = df['Timestamp'].astype(str)

    return df

# Para hacer pruebas
""" x = datetime(2023, 2, 17)
y = datetime(2023, 2, 25)
print(selectinfluxplc(x,y).head()) """