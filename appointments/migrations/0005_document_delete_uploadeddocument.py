# Generated by Django 4.1 on 2023-11-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointments", "0004_uploadeddocument"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="documents/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(name="UploadedDocument",),
    ]
