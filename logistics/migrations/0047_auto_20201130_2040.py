# Generated by Django 3.1.1 on 2020-11-30 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0046_auto_20201123_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_comission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='commission',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(1)]),
        ),
    ]
