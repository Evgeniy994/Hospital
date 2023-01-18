# Generated by Django 4.1.2 on 2022-11-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_doctor_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="avatar",
            field=models.ImageField(
                blank=True,
                default="../static/images/default_user.png",
                null=True,
                upload_to="avatars",
            ),
        ),
    ]
