# test_gnews.py

import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave do ambiente
api_key = os.getenv('GNEWS_API_KEY')

if not api_key:
    print("ERRO: A variável GNEWS_API_KEY não foi encontrada no arquivo .env ou está vazia.")
else:
    print(f"Tentando usar a chave de API: ...{api_key[-4:]}") # Mostra os últimos 4 dígitos para confirmação

    url = f'https://gnews.io/api/v4/top-headlines?country=br&lang=pt&category=general&apikey={api_key}'

    try:
        print("Fazendo a requisição para a GNews...")
        response = requests.get(url)
        # Lança um erro se a resposta for 4xx ou 5xx
        response.raise_for_status() 

        data = response.json()
        print("\nSUCESSO! A API retornou os dados.")
        print(f"Total de artigos encontrados: {data.get('totalArticles')}")

        # Imprime o título do primeiro artigo, se houver
        if data.get('articles'):
            print(f"Título da primeira notícia: {data['articles'][0]['title']}")

    except requests.exceptions.RequestException as e:
        print(f"\nFALHA! A requisição para a API falhou.")
        print(f"Erro detalhado: {e}")