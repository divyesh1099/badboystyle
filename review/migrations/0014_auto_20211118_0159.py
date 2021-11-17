# Generated by Django 3.2.7 on 2021-11-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_alter_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='images',
        ),
        migrations.AddField(
            model_name='review',
            name='images',
            field=models.ImageField(blank=True, upload_to='user_review_images/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='ReviewImage',
        ),
    ]
