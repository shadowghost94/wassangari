# Generated by Django 5.0 on 2024-07-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_remove_utilisateur_is_superuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="utilisateur",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
    ]
