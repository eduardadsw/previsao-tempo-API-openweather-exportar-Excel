import requests
from urllib.parse import quote
import pandas as pd

API_KEY = "97eee0b8b0ade5e9ae34270031b4dcbe"
cidade = str(input('Insira a cidade: '))

cidade_tratada = quote(cidade)
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_tratada}&appid={API_KEY}&units=metric&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
cidade_nome = requisicao_dic['name']
pais = requisicao_dic['sys']['country']
temperatura = requisicao_dic['main']['temp']
sensacao = requisicao_dic['main']['feels_like']
umidade = requisicao_dic['main']['humidity']
vento_kmh = round(requisicao_dic['wind']['speed'] * 3.6, 1)
descricao = requisicao_dic['weather'][0]['description']

dados_da_tabela = {
        "Cidade": [cidade_nome],
        "Pais": [pais],
        "Temperatura (°C)": [temperatura],
        "Sensação": [sensacao],
        "Umidade": [umidade],
        "Vento Km/h": [vento_kmh],
        "Descricao": [descricao]
}

df = pd.DataFrame(dados_da_tabela)

df.to_excel("relatorio_clima.xlsx", index=False)

print("Planilha Excel gerada com sucesso!")
