# Generated by Django 4.2 on 2023-05-08 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("allocated_at", models.DateTimeField(auto_now_add=True)),
                ("return_date", models.DateTimeField(null=True)),
                ("returned_at", models.DateTimeField(null=True)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="loans",
                        to="copies.copy",
                    ),
                ),
            ],
        ),
    ]
