# Generated by Django 2.1.3 on 2018-11-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='closing_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opening_time',
            field=models.TimeField(),
        ),
    ]
