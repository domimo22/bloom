from django.contrib import admin

# Register your models here.
from .models import Plant

# create a class for the admin-model integration
class PlantAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("name", "species", "notes")

admin.site.register(Plant,PlantAdmin)