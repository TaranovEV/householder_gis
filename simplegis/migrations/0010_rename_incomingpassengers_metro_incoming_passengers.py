# Generated by Django 4.1.3 on 2022-12-03 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplegis', '0009_rename_stationname_busstop_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metro',
            old_name='incomingpassengers',
            new_name='incoming_passengers',
        ),
    ]
