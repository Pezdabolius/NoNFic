# Generated by Django 5.0.3 on 2024-05-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
