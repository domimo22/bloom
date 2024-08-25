from django.db import models

# Create your models here.
class Plant(models.Model):
    #user input fields
    name = models.CharField(max_length=150)
    species = models.CharField(max_length=150)
    outdoor = models.BooleanField()
    notes = models.CharField(max_length=300, blank=True, null=True)

    #fields from perenual api
    light_requirements = models.TextField(null=True, blank=True)
    watering_frequency = models.PositiveIntegerField(null=True, blank=True)
    attracts = models.TextField(null=True, blank=True)
    growth_rate = models.TextField(null=True, blank=True)
    poisonous_to_humans = models.BooleanField(null=True, blank=True)
    care_level = models.TextField(null=True, blank=True)
    plant_type = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)

    # def update_watering_frequency(self):
    #     frequency = get_watering_frequency(self.species)
    #     if frequency is not None:
    #         self.watering_frequency = frequency
    #         self.save()

    # string representation of the class
    def __str__(self):
        #it will return the name
        return self.name 