# Generated by Django 4.1.3 on 2022-12-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("triage", "0027_file_file_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="content",
        ),
        migrations.AddField(
            model_name="file",
            name="content_type",
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="file",
            name="storage_key",
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="file",
            name="file_type",
            field=models.CharField(
                choices=[("S", "Source Code"), ("R", "Scan Result"), ("U", "Unknown")],
                db_index=True,
                default="U",
                max_length=16,
            ),
        ),
    ]
