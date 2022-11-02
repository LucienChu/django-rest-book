# bridge (convertor) between python object and json
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
        # select fields defined in model
        # fields = ['id', 'name', 'description']®