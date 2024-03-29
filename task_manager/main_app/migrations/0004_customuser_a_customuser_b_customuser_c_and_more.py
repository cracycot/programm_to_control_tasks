# Generated by Django 5.0.1 on 2024-01-23 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_alter_task_date_finish_customuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="a",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="customuser",
            name="b",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name="customuser",
            name="c",
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="date_finish",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 1, 23, 22, 14, 7, 166937, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
