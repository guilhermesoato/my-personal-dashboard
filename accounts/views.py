from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer
from rest_framework.permissions import AllowAny

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

