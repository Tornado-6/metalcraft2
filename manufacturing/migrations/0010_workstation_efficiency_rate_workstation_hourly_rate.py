# Generated by Django 4.2.7 on 2024-12-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manufacturing", "0009_workstation_process_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workstation",
            name="efficiency_rate",
            field=models.DecimalField(
                decimal_places=2,
                default=1.0,
                help_text="Efficiency rate (1.00 = 100% efficiency, higher values indicate more time/cost needed)",
                max_digits=5,
            ),
        ),
        migrations.AddField(
            model_name="workstation",
            name="hourly_rate",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                help_text="Hourly operational cost for this workstation",
                max_digits=10,
            ),
        ),
    ]