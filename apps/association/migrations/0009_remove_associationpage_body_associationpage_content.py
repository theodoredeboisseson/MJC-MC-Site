# Generated by Django 5.1.6 on 2025-02-25 09:46

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0008_rename_card_image_associationpage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associationpage',
            name='body',
        ),
        migrations.AddField(
            model_name='associationpage',
            name='content',
            field=wagtail.fields.RichTextField(default='', verbose_name='Contenu'),
        ),
    ]
