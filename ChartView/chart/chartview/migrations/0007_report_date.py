# Generated by Django 5.0.2 on 2024-02-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartview', '0006_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
