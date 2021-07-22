# Generated by Django 3.1.3 on 2021-07-22 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sic", "0049_webmention"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvitationRequest",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("address", models.EmailField(max_length=254, unique=True)),
                ("about", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="InvitationRequestVote",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("in_favor", models.BooleanField(blank=True, default=True, null=True)),
                ("note", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="sic.invitationrequest",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "request")},
            },
        ),
    ]
