# Generated by Django 4.0.1 on 2022-01-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_slug'),
        ('cart', '0007_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ManyToManyField(related_name='products', to='product.Product'),
        ),
    ]
