# Generated by Django 4.2.16 on 2024-09-17 09:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid license plate registration number in the format "00AA00" or "00-00-AA".', regex='^\\d{2}[A-Z]{2}\\d{2}$|^\\d{2}-\\d{2}-[A-Z]{2}$')])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]
