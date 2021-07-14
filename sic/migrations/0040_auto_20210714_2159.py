# Generated by Django 3.1.3 on 2021-07-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sic", "0039_auto_20210713_1755"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="kind",
            field=models.CharField(
                choices=[
                    ("RE", "New reply"),
                    ("MEN", "Mention"),
                    ("MSG", "New message"),
                    ("MODR", "A moderator acted on your behalf"),
                    ("OTHR", "New notification"),
                ],
                default="OTHR",
                max_length=4,
            ),
        ),
    ]
