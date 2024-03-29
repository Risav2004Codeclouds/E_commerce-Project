# Generated by Django 5.0 on 2024-01-04 05:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='Product_images/img')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(choices=[('New', 'New'), ('Old', 'Old')], max_length=100)),
                ('information', models.TextField()),
                ('description', models.TextField()),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out Of Stock')], max_length=100)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.brand')),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.categories')),
                ('Color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.color')),
                ('Filter_Price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.filter_price')),
            ],
        ),
    ]
