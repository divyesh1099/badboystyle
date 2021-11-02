# Generated by Django 3.2.7 on 2021-11-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color_of_item', to='product.color'),
        ),
    ]
