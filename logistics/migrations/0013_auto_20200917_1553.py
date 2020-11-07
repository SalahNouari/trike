# Generated by Django 3.1.1 on 2020-09-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0012_auto_20200917_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
