# Generated by Django 4.1.7 on 2023-11-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointmentrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
