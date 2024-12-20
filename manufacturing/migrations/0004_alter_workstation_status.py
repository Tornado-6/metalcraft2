# Generated by Django 4.2.7 on 2024-12-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "manufacturing",
            "0003_alter_workorder_options_workorder_blocking_reason_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="workstation",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACTIVE", "Active"),
                    ("INACTIVE", "Inactive"),
                    ("MAINTENANCE", "Maintenance"),
                ],
                max_length=20,
            ),
        ),
    ]
