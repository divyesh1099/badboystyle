# Generated by Django 3.2.7 on 2021-11-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_review'),
        ('review', '0012_alter_reviewimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_of_review', to='product.product'),
        ),
    ]