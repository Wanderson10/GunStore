# Generated by Django 4.1.5 on 2023-04-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Atributes",
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
                ("calibre", models.CharField(blank=True, max_length=100)),
                ("sistem", models.CharField(blank=True, max_length=100)),
                ("capacidade", models.CharField(blank=True, max_length=100)),
                ("peso", models.CharField(blank=True, max_length=100)),
                ("comprimento", models.CharField(blank=True, max_length=100)),
                ("material", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]