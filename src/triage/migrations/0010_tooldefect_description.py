# Generated by Django 4.0 on 2021-12-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0009_tooldefect_priority_tooldefect_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tooldefect',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
