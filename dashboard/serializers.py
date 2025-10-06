from rest_framework import serializers

# --- Serializers aninhados para o Clima ---
# Representa o dicionário 'main' dentro da resposta do clima
class WeatherMainSerializer(serializers.Serializer):
    temp = serializers.FloatField()
    feels_like = serializers.FloatField()

# Representa cada item na lista 'weather'
class WeatherInfoSerializer(serializers.Serializer):
    description = serializers.CharField()

# Serializer principal para os dados do clima
class WeatherSerializer(serializers.Serializer):
    main = WeatherMainSerializer()
    weather = WeatherInfoSerializer(many=True) # many=True porque 'weather' é uma lista

# Serializer principal para cada artigo de notícia
class NewsArticleSerializer(serializers.Serializer):
    source_name = serializers.CharField(source='source.name') 
    title = serializers.CharField()
    url = serializers.URLField()

# --- Serializer aninhado para as Cotações ---
class QuoteDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    bid = serializers.CharField() # 'bid' é o valor da cotação


# --- O SERIALIZER PRINCIPAL QUE JUNTA TUDO ---
class DashboardDataSerializer(serializers.Serializer):
    weather = WeatherSerializer(required=False, allow_null=True)
    news = NewsArticleSerializer(many=True, required=False, allow_null=True)
    quotes = serializers.DictField(child=QuoteDetailSerializer(), required=False, allow_null=True)