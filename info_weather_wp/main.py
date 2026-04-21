import json

# No modo "Run Once for All Items" usa-se _items
localizacao = items('HTTP_R_Location')[0].json
clima = items('HTTP_R_Weather')[0].json
texto_frase = items('B_LLM_C_Phrase')[0].json['text']
frase = json.loads(texto_frase)['Frase Motivacional']

# Mapeando os códigos de clima para descrições e emojis
def interpretar_clima(codigo):
    if codigo == 0:         return '☀️ Céu limpo'
    elif codigo <= 2:       return '🌤️ Parcialmente nublado'
    elif codigo == 3:       return '☁️ Nublado'
    elif codigo <= 49:      return '🌫️ Neblina'
    elif codigo <= 59:      return '🌦️ Garoa'
    elif codigo <= 69:      return '🌧️ Chuva'
    elif codigo <= 79:      return '🌨️ Neve'
    elif codigo <= 84:      return '🌧️ Chuva forte'
    elif codigo <= 99:      return '⛈️ Tempestade'
    else:                   return '🌡️ Indefinido'

# Cabeçalho com clima atual
clima_atual = clima['current_weather']
cabecalho = (
    f"🌍 *{localizacao['city']}, {localizacao['regionName']}*\n"
    f"📅 Hoje — {interpretar_clima(clima_atual['weathercode'])}\n"
    f"🌡️ Temperatura atual: {clima_atual['temperature']}°C\n"
    f"💨 Vento: {clima_atual['windspeed']} km/h\n"
)

# Previsão dos 7 dias
linhas = []
for i, data in enumerate(clima['daily']['time']):
    linha = (
        f"{interpretar_clima(clima['daily']['weathercode'][i])} *{data}*\n"
        f"   🌡️ {clima['daily']['temperature_2m_min'][i]}°C ~ {clima['daily']['temperature_2m_max'][i]}°C\n"
        f"   💧 Chuva: {clima['daily']['precipitation_probability_max'][i]}%"
    )
    linhas.append(linha)

previsao = '\n\n'.join(linhas)

# Montando a mensagem final
mensagem = (
    f"{cabecalho}\n"
    f"━━━━━━━━━━━━━━━━\n"
    f"📆 *Previsão dos próximos 7 dias*\n\n"
    f"{previsao}\n\n"
    f"━━━━━━━━━━━━━━━━\n"
    f"💬 {frase}"
)

return [{'json': {'message': mensagem}}]