# Generated by Django 3.2.7 on 2021-12-01 08:55

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='products/default.jpg', upload_to='products/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping', models.FloatField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=1000, unique=True)),
            ],
            options={
                'ordering': ['size'],
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_dimension_LxWxH', models.CharField(blank=True, max_length=200, null=True)),
                ('date_first_available', models.DateField(auto_now_add=True, null=True)),
                ('manufacturer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('country_of_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, default='PRODUCT', max_length=100, null=True)),
                ('manufacturer_address', models.CharField(blank=True, max_length=500, null=True)),
                ('packer_address', models.CharField(blank=True, max_length=500, null=True)),
                ('item_weight', models.FloatField(blank=True, null=True)),
                ('net_quantity', models.IntegerField(blank=True, null=True)),
                ('included_components', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='types/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('stock', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.FloatField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('generated_variation_id', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color_of_variation', to='product.color')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='size_of_variation', to='product.size')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField()),
                ('detail', models.TextField()),
                ('stock', models.PositiveBigIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('image', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_of_product', to='product.productimage')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_of_product', to='offer.offer')),
                ('specification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specification_of_product', to='product.specification')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_of_product', to='product.type')),
                ('variations', models.ManyToManyField(blank=True, related_name='variation_of_product', to='product.Variation')),
            ],
            options={
                'ordering': ['edited'],
            },
        ),
    ]
