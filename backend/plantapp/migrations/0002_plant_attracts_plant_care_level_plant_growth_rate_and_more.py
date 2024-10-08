# Generated by Django 4.2.15 on 2024-08-24 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plantapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="attracts",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="plant",
            name="care_level",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="plant",
            name="growth_rate",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="plant",
            name="light_requirements",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="plant",
            name="outdoor",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="plant",
            name="plant_type",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="plant",
            name="poisonous_to_humans",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="plant",
            name="watering_frequency",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="plant",
            name="notes",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
