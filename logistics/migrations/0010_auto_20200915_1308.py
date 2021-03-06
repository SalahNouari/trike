# Generated by Django 3.1.1 on 2020-09-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0009_seller_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='banner',
            new_name='thumbnail',
        ),
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='photos/sellers/%Y/%m/%d/'),
        ),
    ]
