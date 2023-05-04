# Generated by Django 4.1.5 on 2023-05-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weapons", "0004_alter_weapon_descripition"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="weapon",
            name="group",
        ),
        migrations.AlterField(
            model_name="weapon",
            name="tipe",
            field=models.CharField(
                choices=[
                    ("Guns", "Guns"),
                    ("Knife", "Knife"),
                    ("Bow", "Bow"),
                    ("CrossBow", "Crossbow"),
                    ("Uniformed", "Uninformed"),
                ],
                default="Uniformed",
                max_length=10,
            ),
        ),
    ]
