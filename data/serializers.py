from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import DataModel

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataModel
        fields = '__all__'

