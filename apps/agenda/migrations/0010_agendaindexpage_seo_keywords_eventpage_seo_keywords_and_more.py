# Generated by Django 5.1.6 on 2025-03-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_alter_eventpage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendaindexpage',
            name='seo_keywords',
            field=models.CharField(blank=True, help_text='Comma-separated keywords specific to this page', max_length=255),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='seo_keywords',
            field=models.CharField(blank=True, help_text='Comma-separated keywords specific to this page', max_length=255),
        ),
        migrations.AddField(
            model_name='pasteventspage',
            name='seo_keywords',
            field=models.CharField(blank=True, help_text='Comma-separated keywords specific to this page', max_length=255),
        ),
    ]
