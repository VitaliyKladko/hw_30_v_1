# Generated by Django 4.2.1 on 2023-05-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_selection"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="selection",
            constraint=models.UniqueConstraint(
                fields=("name", "owner"), name="my_constraint"
            ),
        ),
    ]
