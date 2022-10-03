from rest_framework import serializers
from main.models import Flyings, Company


class flysserializer(serializers.ModelSerializer):
    class Meta:
        model = Flyings
        fields = ['fr', 'to', 'wh', 'price', 'co', 'Company_id']


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'text']