# Generated by Django 4.2 on 2023-05-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_rename_afferword_book_afterword"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(default=None),
        ),
    ]