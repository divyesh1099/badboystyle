# Generated by Django 3.2.7 on 2021-11-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_alter_offer_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='product',
        ),
    ]