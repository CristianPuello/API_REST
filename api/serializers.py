from rest_framework import serializers
from .models import Jokes


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jokes
        fields = ('__all__')
