# dashboard/views.py

import requests
from django.shortcuts import render
from django.conf import settings # Importa as configurações do Django

def dashboard_view(request):
    # Dados do Clima
    weather_data = None
    city = 'Brasilia' # Cidade fixa por enquanto
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

    try:
        response = requests.get(url)
        response.raise_for_status() # Lança um erro para respostas HTTP ruins (4xx ou 5xx)
        weather_data = response.json()
    except requests.exceptions.RequestException as e:
        # Aqui você pode logar o erro, mostrar uma mensagem, etc.
        print(f"Error fetching weather data: {e}")
        # weather_data continua como None

    context = {
        'usuario': 'Visitante',
        'weather': weather_data,
    }
    return render(request, 'dashboard/home.html', context)