# Generated by Django 5.1.6 on 2025-03-06 14:38

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylist',
            name='content',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='Contenu'),
        ),
    ]
