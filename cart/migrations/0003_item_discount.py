# Generated by Django 3.2.6 on 2021-09-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
