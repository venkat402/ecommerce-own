# Generated by Django 4.0.1 on 2022-01-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_cartitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ManyToManyField(related_name='carts', to='cart.Cart'),
        ),
    ]
