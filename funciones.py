import requests, json
from datetime import datetime,timedelta
from mastodon import Mastodon

mañana = str(datetime.now()+timedelta(days=1))

def peticion_aemet(url,headers,querystring):

    response = requests.request("GET", url, headers=headers, params=querystring)

    dict = json.loads(response.text)
    datos = dict["datos"]

    respuesta = requests.request("GET", datos, headers=headers)

    resultado = json.loads(respuesta.text)

    return resultado

def obtener_datos(resultado):
    prediccion = {}
    estadoCielo = []
    precipitacion = []
    temperatura = []
    fecha = (datetime.now()+timedelta(days=1)).strftime("%d/%m/%y - %I:%M %p")
    for dia in resultado[0]["prediccion"]["dia"]:
        for campo,valor in dia.items():
            if campo == "estadoCielo":
                for hora in valor:
                    for campo,valor in hora.items():
                        if campo == "periodo" and valor == mañana[11:13]:
                            estadoCielo.append(hora["descripcion"])
            elif campo == "precipitacion":
                for hora in valor:
                    for campo,valor in hora.items():
                        if campo == "periodo" and valor == mañana[11:13]:
                            precipitacion.append(hora["value"])
            elif campo == "temperatura":
                for hora in valor:
                    for campo,valor in hora.items():
                        if campo == "periodo" and valor == mañana[11:13]:
                            temperatura.append(hora["value"])
    prediccion["estadoCielo"] = estadoCielo[1]
    prediccion["precipitacion"] = precipitacion[1]
    prediccion["temperatura"] = temperatura[1]
    prediccion["fecha"] = fecha
    return prediccion

def escribir_mensaje(datos):
    if datos["estadoCielo"] == "Despejado":
        estadoCielo = "☀️"
    elif datos["estadoCielo"] == "Poco nuboso" or datos["estadoCielo"] == "Intervalos nubosos":
        estadoCielo = "🌤️"
    elif datos["estadoCielo"] == "Nuboso con lluvia escasa" or datos["estadoCielo"] == "Intervalos nubosos con lluvia escasa":
        estadoCielo = "🌦️​"
    elif datos["estadoCielo"] == "Cubierto con lluvia escasa":
        estadoCielo = "☁️​💧"
    else:
        estadoCielo = "Estado del cielo"
    
    if int(datos["precipitacion"]) >= 2:
        precipitacion = "☔"
    elif int(datos["precipitacion"]) < 2 and int(datos["precipitacion"]) > 0:
        precipitacion = "☂️"
    elif int(datos["precipitacion"]) == 0:
        precipitacion = "🌂"
    else:
        precipitacion = "Precipitación"

    if int(datos["temperatura"]) >= 35:
        temperatura = "🔥"
    elif int(datos["temperatura"]) < 35 and int(datos["temperatura"]) >= 10:
        temperatura = "🌡️"
    elif int(datos["temperatura"]) < 10:
        temperatura = "❄️"
    else:
        temperatura = "Temperatura"
    
    mensaje = f'''Predicción del tiempo para Dos Hermanas:
{datos["fecha"]}
{estadoCielo}  {datos["estadoCielo"]}
{precipitacion}  {datos["precipitacion"]} mm
{temperatura}  {datos["temperatura"]} ºC'''
    
    return (mensaje)

def publicar_mensaje(mensaje, client_id, client_secret, access_token, api_base_url):
    m = Mastodon(client_id=client_id, client_secret=client_secret, access_token=access_token, api_base_url=api_base_url)
    m.status_post(mensaje)