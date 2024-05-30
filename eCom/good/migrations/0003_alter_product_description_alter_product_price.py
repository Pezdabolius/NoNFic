# Generated by Django 5.0.3 on 2024-05-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]