# Generated by Django 3.2.7 on 2021-11-07 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_of_review', to='review.reviewimage'),
        ),
        migrations.AlterField(
            model_name='reviewimage',
            name='image',
            field=models.ImageField(blank=True, default='None', null=True, upload_to='user_review_images/%Y/%m/%d/'),
        ),
    ]
