# Generated by Django 4.2.4 on 2023-09-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerce", "0005_alter_productmodel_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
