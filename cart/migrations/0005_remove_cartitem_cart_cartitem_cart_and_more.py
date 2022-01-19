# Generated by Django 4.0.1 on 2022-01-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_slug'),
        ('cart', '0004_alter_cartitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ManyToManyField(to='cart.Cart'),
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
