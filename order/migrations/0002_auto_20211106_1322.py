# Generated by Django 3.2.7 on 2021-11-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Total',
        ),
    ]