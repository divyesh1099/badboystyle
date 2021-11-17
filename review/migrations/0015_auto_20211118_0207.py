# Generated by Django 3.2.7 on 2021-11-17 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0014_auto_20211118_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_review_images/%Y/%m/%d/')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
    ]