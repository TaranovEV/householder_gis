# Generated by Django 4.1.3 on 2022-12-01 17:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("simplegis", "0005_metro"),
    ]

    operations = [
        migrations.RenameField(
            model_name="metro",
            old_name="IncomingPassangers",
            new_name="IncomingPassengers",
        ),
    ]
