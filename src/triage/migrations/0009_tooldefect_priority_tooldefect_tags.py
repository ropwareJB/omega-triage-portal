# Generated by Django 4.0 on 2021-12-13 21:00

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('triage', '0008_alter_finding_managers_remove_finding_analyst_impact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tooldefect',
            name='priority',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tooldefect',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]