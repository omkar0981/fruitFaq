from rest_framework import serializers

from .models import FruitFaq


class FruitFaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = FruitFaq
        fields = '__all__'
