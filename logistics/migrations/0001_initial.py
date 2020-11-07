# Generated by Django 3.1 on 2020-08-24 02:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=15, null=True)),
                ('activity_type', models.CharField(max_length=125)),
                ('shipping', models.DecimalField(decimal_places=2, default=50, max_digits=10)),
                ('loc1_latitude', models.CharField(blank=True, max_length=25, null=True)),
                ('loc1_longitude', models.CharField(blank=True, max_length=25, null=True)),
                ('loc2_latitude', models.CharField(max_length=25)),
                ('loc2_longitude', models.CharField(max_length=25)),
                ('contact_number', models.CharField(blank=True, max_length=125, null=True)),
                ('auth_id', models.CharField(blank=True, max_length=125, null=True)),
                ('capture_id', models.CharField(blank=True, max_length=125, null=True)),
                ('cod', models.BooleanField(default=False)),
                ('pickup', models.BooleanField(default=False)),
                ('pickup_address', models.CharField(blank=True, max_length=125, null=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('date_paid', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('description', models.TextField(default='', max_length=4000)),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('sale_price_start_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('sale_price_end_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('orders', models.PositiveIntegerField(default=0)),
                ('date_published', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(to='logistics.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('loc1_latitude', models.CharField(blank=True, max_length=25, null=True)),
                ('loc1_longitude', models.CharField(blank=True, max_length=25, null=True)),
                ('banner', models.ImageField(blank=True, upload_to='photos/sellers/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='RiderReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1)),
                ('comment', models.TextField(blank=True, max_length=4000, null=True)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riders_reviews', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rider_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1)),
                ('comment', models.TextField(blank=True, max_length=4000, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_reviews', to='logistics.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='logistics.seller'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(blank=True, null=True)),
                ('ordered_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('date_delivered', models.DateTimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='logistics.activity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='logistics.product')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='logistics.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_group', to='logistics.categorygroup'),
        ),
        migrations.AddField(
            model_name='activity',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.seller'),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
