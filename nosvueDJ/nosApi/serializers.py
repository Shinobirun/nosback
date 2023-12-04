from django.contrib.auth.models import User  
from rest_framework import serializers
from .models import User, PaqueteTuristico, HistorialViajes

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = '__all__'

class PaqueteTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteTuristico
        fields = '__all__'

class HistorialViajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialViajes
        fields = '__all__'

class ApiTokenObtainPairSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True, label="Username")
    description = serializers.CharField(max_length=255, required=True, label="Password")
