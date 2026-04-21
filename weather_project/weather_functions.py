import requests #Me possibilita receber requests dos sites.
import json #Me permite trabalhar com json.
from datetime import datetime, timedelta #Trabalhar com datas da melhor maneira possível"



# Função que pega a localização do usuário (lat e lon):
def current_location():
    url_local = "http://ip-api.com/json/"
    r1 = requests.get(url_local)

    if r1.status_code != 200:
        print("Não foi possível obter a localização.")
    else:
        local_json = json.loads(r1.text)
        return local_json



# Função que fornece o json que contem todas as informações das condições climáticas atuais e futuras:
def current_conditions(lat, lon):
    url_part_openmeteo = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "apparent_temperature_max",
                  "apparent_temperature_min", "precipitation_sum", "precipitation_probability_max", "rain_sum",
                  "sunrise", "sunset", "uv_index_max", "relative_humidity_2m_mean", "wind_speed_10m_max",
                  "wind_gusts_10m_mean", "cloud_cover_mean", "temperature_2m_mean", "wind_gusts_10m_max"],
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "precipitation", "rain",
                    "showers", "snowfall"],
        "timezone": "auto",
    }
    r2 = requests.get(url_part_openmeteo, params=params)
    if r2.status_code != 200:
        print("Não foi possível obter as condições climáticas.")
        return None
    else:
        weather_json = json.loads(r2.text)
        return weather_json



#Função que printa as condições climáticas atuais:
def show_current_weather(current, units):
    try:
        print(f"🗓️️  Data:             {current['time'][8:10] + "/" + current['time'][5:7] + "/" + current['time'][:4]}")
        print(f"🌡️  Temperatura:      {current['temperature_2m']} {units['temperature_2m']}")
        print(f"🤔  Sensação térmica: {current['apparent_temperature']} {units['apparent_temperature']}")
        print(f"💧  Umidade relativa: {current['relative_humidity_2m']} {units['relative_humidity_2m']}")
        print(f"🌧️  Precipitação:     {current['precipitation']} {units['precipitation']}")
        print(f"🌂  Chuva:            {current['rain']} {units['rain']}\n")
        return None
    except:
        print("ERRO na função 'show_current_weather(current, units)'. Provavelmente o json foi alterado pelo site da API.")



# Utilizando o timedelta de datetime para facilitar o fornecimento de data atual + 6 dias.
def datafinal(current):
    try:
        current_date = datetime.strptime(current['time'], "%Y-%m-%dT%H:%M")
        data_final = (current_date + timedelta(days=6)).strftime("%d/%m/%Y")
        return data_final
    except:
        print("Erro na função 'datafinal(current)'.")



#Função de traduzir o Weather-code
def weather_code(codigo):
    tabela = {
        0:  "☀️  Céu limpo",
        1:  "🌤️  Principalmente limpo",
        2:  "⛅  Parcialmente nublado",
        3:  "☁️  Nublado",
        45: "🌫️  Neblina",
        48: "🌫️  Neblina com geada",
        51: "🌦️  Garoa leve",
        53: "🌦️  Garoa moderada",
        55: "🌦️  Garoa intensa",
        61: "🌧️  Chuva leve",
        63: "🌧️  Chuva moderada",
        65: "🌧️  Chuva intensa",
        71: "🌨️  Neve leve",
        73: "🌨️  Neve moderada",
        75: "🌨️  Neve intensa",
        77: "🌨️  Granizo",
        80: "🌦️  Pancadas de chuva leves",
        81: "🌦️  Pancadas de chuva moderadas",
        82: "🌦️  Pancadas de chuva fortes",
        85: "🌨️  Pancadas de neve leves",
        86: "🌨️  Pancadas de neve intensas",
        95: "⛈️  Tempestade",
        96: "⛈️  Tempestade com granizo leve",
        99: "⛈️  Tempestade com granizo intenso",
    }
    return tabela.get(codigo, "❓ Código desconhecido")



#Função que printa as condições climáticas dos próximos 6 dias e do atual:
def weather_7days(daily, du):
    try:
        for day in range(len(daily['time'])):
            print(f"🗓️️  Data:                   {daily['time'][day][8:10] + "/" + daily['time'][day][5:7] + "/" + daily['time'][day][:4]}")
            print(f"🌤️  Clima do dia:           {weather_code(daily['weather_code'][day])}") #Usa a função weather_code(codigo)
            print(f"🌡️  Temperatura máxima:     {daily['temperature_2m_max'][day]} {du['temperature_2m_max']}")
            print(f"🌡️  Temperatura mínima:     {daily['temperature_2m_min'][day]} {du['temperature_2m_min']}")
            print(f"🥵  Sensação máxima:        {daily['apparent_temperature_max'][day]} {du['apparent_temperature_max']}")
            print(f"🥶  Sensação mínima:        {daily['apparent_temperature_min'][day]} {du['apparent_temperature_min']}")
            print(f"🌡️  Temperatura média:      {daily['temperature_2m_mean'][day]} {du['temperature_2m_mean']}")
            print(f"🌧️  Precipitação total:     {daily['precipitation_sum'][day]} {du['precipitation_sum']}")
            print(f"☔  Prob. máx. de chuva:    {daily['precipitation_probability_max'][day]} {du['precipitation_probability_max']}")
            print(f"🌂  Chuva total:            {daily['rain_sum'][day]} {du['rain_sum']}")
            print(f"🌅  Nascer do sol:          {daily['sunrise'][day][11:16]}h")
            print(f"🌇  Pôr do sol:             {daily['sunset'][day][11:16]}h")
            print(f"🔆  Índice UV máximo:       {daily['uv_index_max'][day]}")
            print(f"💧  Umidade relativa média: {daily['relative_humidity_2m_mean'][day]} {du['relative_humidity_2m_mean']}")
            print(f"💨  Velocidade máx. vento:  {daily['wind_speed_10m_max'][day]} {du['wind_speed_10m_max']}")
            print(f"🌬️  Rajadas médias:         {daily['wind_gusts_10m_mean'][day]} {du['wind_gusts_10m_mean']}")
            print(f"☁️  Cobertura de nuvens:    {daily['cloud_cover_mean'][day]} {du['cloud_cover_mean']}")
            print("\n")
        return None
    except:
        print("ERRO na função 'weather_7days(daily, du)'. Provavelmente o json foi alterado pelo site da API.")