# Generated by Django 4.0.5 on 2023-07-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price'),
        ),
    ]
