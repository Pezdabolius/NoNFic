# Generated by Django 5.0.3 on 2024-05-12 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='good_catego_name_78a25c_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=1000)),
                ('available', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.ImageField(upload_to='goods/%Y')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='good.category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
