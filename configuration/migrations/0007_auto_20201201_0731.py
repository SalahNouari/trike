# Generated by Django 3.1.1 on 2020-11-30 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0006_auto_20201113_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='per_km_price',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='motorcycle_per_km_price',
            field=models.PositiveIntegerField(default=35),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='tricycle_per_km_price',
            field=models.PositiveIntegerField(default=45),
        ),
    ]
