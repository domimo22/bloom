# Create your views here.
from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the PlantSerializer from the serializer file
from .serializers import PlantSerializer

# import the Plant model from the models file
from .models import Plant

# create a class for the Plant model viewsets
class PlantView(viewsets.ModelViewSet):

    # create a serializer class and 
    # assign it to the PlantSerializer class
    serializer_class = PlantSerializer

    # define a variable and populate it 
    # with the Plant objects
    queryset = Plant.objects.all()

    # def perform_update(self, serializer):
    #     plant = serializer.save()
    #     plant.update_watering_frequency()