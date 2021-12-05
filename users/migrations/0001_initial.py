# Generated by Django 3.2.7 on 2021-12-01 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='user/profile/default.jpg', upload_to='user/profile/%Y/%m/%d/')),
                ('phonenumber', models.PositiveBigIntegerField(blank=True, default=0)),
                ('state', models.CharField(blank=True, default='Maharashtra', max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.PositiveIntegerField(blank=True, default=400709)),
                ('address', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
