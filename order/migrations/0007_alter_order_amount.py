# Generated by Django 3.2.7 on 2021-11-05 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.total'),
        ),
    ]