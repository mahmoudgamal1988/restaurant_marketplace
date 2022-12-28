# Generated by Django 4.1.1 on 2022-10-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(1, "Restaurant"), (2, "Customer")], null=True
            ),
        ),
    ]
