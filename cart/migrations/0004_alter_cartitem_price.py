# Generated by Django 4.0.1 on 2022-01-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
