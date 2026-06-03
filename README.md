# previsao-tempo-python-API-openweather-exportar-Excel

Este é um projeto prático desenvolvido em Python que consome dados em tempo real da API meteorológica OpenWeather, realiza o tratamento e conversão das informações e exporta um relatório estruturado diretamente para uma planilha do Excel (.xlsx).

Funcionalidades:

Integração em Tempo Real: Conexão direta com a API OpenWeather (rota Current Weather Data).
Tratamento de Entrada de Dados: Utilização de codificação de URL urllib.parse.quote para garantir que cidades com espaços ou acentos.
Estruturação com Pandas: Organização dos dados brutos do JSON em um DataFrame estruturado.
Exportação Automatizada: Geração de arquivo Excel limpo pronto para uso corporativo.
Transformação de Métricas: Conversão automática da velocidade do vento de m/s para km/h.

Tecnologias Utilizadas:

Python 3 (Linguagem base)
Requests (Para chamadas HTTP/API)
Pandas (Para manipulação e estruturação de tabelas)
OpenPyXL (Engine para criação de arquivos `.xlsx`)
Urllib (Biblioteca padrão do Python para tratamento de URLs)

