# Generated by Django 4.0.3 on 2022-04-30 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bid", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bid",
            old_name="auctoin",
            new_name="auction",
        ),
    ]
