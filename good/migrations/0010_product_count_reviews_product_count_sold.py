# Generated by Django 5.0.3 on 2024-08-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0009_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_reviews',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='count_sold',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
