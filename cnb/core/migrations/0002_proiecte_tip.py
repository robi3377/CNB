# Generated by Django 4.2.1 on 2023-05-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proiecte',
            name='tip',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
