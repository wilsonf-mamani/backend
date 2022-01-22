from rest_framework import serializers
from .models import PersonaModel

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaModel
        fields = '__all__'