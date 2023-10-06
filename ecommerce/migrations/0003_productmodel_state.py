# Generated by Django 4.2.4 on 2023-09-19 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "ecommerce",
            "0002_productmodel_color_productmodel_description_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="state",
            field=models.CharField(
                choices=[
                    ("BR", "BORRADOR"),
                    ("PU", "PUBLICADO"),
                    ("PR", "PRIVADO"),
                ],
                default="BR",
                max_length=2,
            ),
        ),
    ]
