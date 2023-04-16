import requests


from datetime import datetime

agora = datetime.now()
data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data e hora:", data_hora_formatada)

API_KEY = "815669c352784ab9a7588517e108fc8a"

city_name = input("Digite o nome da cidade: ")

link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic= requisicao.json()
descricao = requisicao_dic['weather'] [0] ['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
temperatura= round(temperatura, 2)
print(descricao, f"{temperatura}°C")
