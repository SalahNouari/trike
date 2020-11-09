# Generated by Django 3.1.1 on 2020-11-08 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logistics', '0038_auto_20201014_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorygroup',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='rider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claimed_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='logistics.seller'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CommissionPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=15, null=True)),
                ('date_paid', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission_payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
