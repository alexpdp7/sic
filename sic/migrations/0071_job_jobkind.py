# Generated by Django 3.2.6 on 2021-08-16 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sic", "0070_story_karma"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobKind",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("dotted_path", models.TextField(unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
                ("periodic", models.BooleanField(default=False)),
                ("failed", models.BooleanField(default=False)),
                ("last_run", models.DateTimeField(blank=True, default=None, null=True)),
                ("logs", models.TextField(blank=True, null=True)),
                ("data", models.JSONField(blank=True, null=True)),
                (
                    "kind",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="sic.jobkind",
                    ),
                ),
            ],
        ),
    ]
