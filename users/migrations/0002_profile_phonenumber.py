# Generated by Django 3.2.7 on 2021-11-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phonenumber',
            field=models.PositiveBigIntegerField(default=9920192856),
            preserve_default=False,
        ),
    ]