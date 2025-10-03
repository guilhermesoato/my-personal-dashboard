import requests
from django.shortcuts import render
from django.conf import settings

def dashboard_view(request):
    # --- Dados do Clima ---
    weather_data = None
    try:
        city = 'Brasilia'
        api_key = settings.OPENWEATHERMAP_API_KEY
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

    # --- Dados das Notícias ---
    news_data = None
    try:
        api_key = settings.GNEWS_API_KEY
        url = f'https://gnews.io/api/v4/top-headlines?country=br&lang=pt&category=general&apikey={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news data: {e}")

    # --- Dados de Cotações ---
    quotes_data = None
    try:
        # Dólar, Euro e Bitcoin
        url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
        response = requests.get(url)
        response.raise_for_status()
        quotes_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quotes data: {e}")


    context = {
        'usuario': 'Visitante',
        'weather': weather_data,
        'news': news_data,
        'quotes': quotes_data, 
    }
    return render(request, 'dashboard/home.html', context)