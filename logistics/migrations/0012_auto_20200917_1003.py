# Generated by Django 3.1.1 on 2020-09-17 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0011_auto_20200915_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_6',
        ),
    ]
