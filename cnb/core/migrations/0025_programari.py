# Generated by Django 4.2.1 on 2023-05-25 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_olimpici_poza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=255)),
                ('data', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
