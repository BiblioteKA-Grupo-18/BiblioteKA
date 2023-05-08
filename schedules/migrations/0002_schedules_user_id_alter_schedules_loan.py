# Generated by Django 4.2 on 2023-05-07 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("loans", "0003_alter_loan_return_date_alter_loan_returned_at"),
        ("schedules", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedules",
            name="user_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="schedules",
            name="loan",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="schedule",
                to="loans.loan",
            ),
        ),
    ]
