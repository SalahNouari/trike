# Generated by Django 3.1.1 on 2020-12-01 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0050_order_two_way'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered_comission',
            new_name='ordered_commission',
        ),
    ]
