# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Plant

# create a serializer class
class PlantSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Plant
        fields = ("name", "species", "notes")

    #OVERIDES the built-in create method for POST requests
    #this makes it so some fields are optional for POST, but are still included in GET
    # def create(self, validated_data):
    #     # 'watering_frequency' is not required when creating a new plant
    #     plant = Plant.objects.create(**validated_data)
    #     # Optionally, set 'watering_frequency' after creation
    #     plant.update_watering_frequency()
    #     return plant