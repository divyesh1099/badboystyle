# Generated by Django 3.2.7 on 2021-11-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_rating'),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.ManyToManyField(related_name='product_of_offer', to='product.Product'),
        ),
    ]
