from django.contrib.auth.models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # write_only para que a senha não seja retornada na resposta da API
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data.get('email', '')
        new_user = User(username=username, email=email)
        new_user.set_password(password) # Usa o método set_password para garantir que a senha seja criptografada
        new_user.save()
        return new_user