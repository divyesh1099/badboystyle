# Generated by Django 3.2.7 on 2021-12-07 09:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]