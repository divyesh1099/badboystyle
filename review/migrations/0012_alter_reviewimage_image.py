# Generated by Django 3.2.7 on 2021-11-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0011_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimage',
            name='image',
            field=models.ImageField(upload_to='user_review_images/%Y/%m/%d/'),
        ),
    ]
