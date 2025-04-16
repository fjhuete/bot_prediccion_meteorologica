#Predicción_ElTiempo
import funciones, os
from datetime import datetime
from time import sleep

#Declaración de variables

#AEMET
id_municipio = os.environ.get("id_municipio")
url = "https://opendata.aemet.es/opendata//api/prediccion/especifica/municipio/horaria/"+id_municipio
api_key = os.environ.get("api_key")
querystring = {"api_key":api_key}
headers = {
    'cache-control': "no-cache"
    }

#Mastodon
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
access_token = os.environ.get("access_token")
api_base_url = os.environ.get("api_base_url")

#Aplicación
while True:

    ahora = str(datetime.now())
    minutos = ahora[14:16]

    if minutos == "00":

        resultado = funciones.peticion_aemet(url,headers,querystring)

        datos = funciones.obtener_datos(resultado)

        mensaje = funciones.escribir_mensaje(datos)

        funciones.publicar_mensaje(mensaje, client_id, client_secret, access_token, api_base_url)

        sleep(3560)
    
    else:
        sleep(59)