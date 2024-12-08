# Generated by Django 4.2.7 on 2024-12-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manufacturing", "0010_productworkstationsequence"),
    ]

    operations = [
        migrations.AddField(
            model_name="productworkstationsequence",
            name="process_type",
            field=models.CharField(
                choices=[("AUTOMATIC", "Automatic"), ("MANUAL", "Manual")],
                default="MANUAL",
                max_length=20,
            ),
        ),
    ]
