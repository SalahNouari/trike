# Generated by Django 3.1.1 on 2020-09-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200923_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, upload_to='photos/sellers/%Y/%m/%d/'),
        ),
    ]
