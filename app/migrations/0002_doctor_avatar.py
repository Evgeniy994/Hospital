# Generated by Django 4.1.2 on 2022-11-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="avatar",
            field=models.ImageField(
                default="static/images/default_user.png", upload_to=""
            ),
        ),
    ]
