# Generated by Django 4.1.6 on 2023-11-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_room_closetime_room_opentime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='roomId',
            field=models.CharField(max_length=10),
        ),
    ]
