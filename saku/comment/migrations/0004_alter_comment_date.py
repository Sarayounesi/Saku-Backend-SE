# Generated by Django 4.0.5 on 2022-06-17 11:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comment", "0003_alter_comment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
