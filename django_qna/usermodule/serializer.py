from .models import QuizUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizUser
        fields = '__all__'

