# Generated by Django 4.2.4 on 2023-11-24 19:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "forms",
            "0002_userclientmodel_email_userclientmodel_first_name_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userclientmodel",
            name="user",
        ),
    ]
