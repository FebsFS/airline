# Generated by Django 4.0.6 on 2022-08-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flyings',
            name='fr',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='flyings',
            name='to',
            field=models.CharField(max_length=255),
        ),
    ]
