# Generated by Django 4.0.3 on 2022-06-02 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="reply_on",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="comment.comment",
            ),
        ),
    ]
