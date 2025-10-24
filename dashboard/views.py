import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import DashboardDataSerializer

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
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

        news_data = None
        try:
            api_key = settings.GNEWS_API_KEY
            url = f'https://gnews.io/api/v4/top-headlines?country=br&lang=pt&category=general&apikey={api_key}'
            response = requests.get(url)
            response.raise_for_status()
            news_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news data: {e}")

        quotes_data = None
        try:
            url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
            response = requests.get(url)
            response.raise_for_status()
            quotes_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching quotes data: {e}")

        articles_list = []
        if news_data and 'articles' in news_data:
            articles_list = news_data['articles']

        combined_data = {
            'weather': weather_data,
            'news': articles_list,
            'quotes': quotes_data,
        }

        serializer = DashboardDataSerializer(instance=combined_data)

        return Response(serializer.data)