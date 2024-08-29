#Predicción_ElTiempo
import funciones
from datetime import datetime
from time import sleep

#Declaración de variables

#AEMET
url = "https://opendata.aemet.es/opendata//api/prediccion/especifica/municipio/horaria/41038"
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmamh1ZXRlLm1AZ21haWwuY29tIiwianRpIjoiODRkYTI0ZWEtNDcxYS00NDY4LWI0Y2UtNTQ1YWZhNGIyNzY1IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3MTQ0OTczMzMsInVzZXJJZCI6Ijg0ZGEyNGVhLTQ3MWEtNDQ2OC1iNGNlLTU0NWFmYTRiMjc2NSIsInJvbGUiOiIifQ.ly82KvHJYWaroA13Mr7QRyyhwQ2Ls9i0-Q8ofa02n8o"
querystring = {"api_key":api_key}
headers = {
    'cache-control': "no-cache"
    }

#Mastodon
client_id = "h-3ArSgPqHwBHcVWUi1yEh2qyYJ1TmntoJqkjZX1_ts"
client_secret = "begNgcdfq8-T7xjbXi_TSvZK8XRqy9rFzLl1xtPTZ0I"
access_token = "YsmX2WVxV6swVxUIFMVsl4yqqUv7-IirmPRu7gA4WmQ"
api_base_url = "https://mastodon.social"

while True:

    ahora = str(datetime.now())
    minutos = ahora[14:16]

    if minutos == "00":

        resultado = funciones.peticion_aemet(url,headers,querystring)

        datos = funciones.obtener_datos(resultado)

        mensaje = funciones.escribir_mensaje(datos)

        funciones.publicar_mensaje(mensaje, client_id, client_secret, access_token, api_base_url)

        sleep(59)
    
    else:
        sleep(59)