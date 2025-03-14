# Generated by Django 5.1.6 on 2025-03-13 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_alter_flashmessage_message'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseindexpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text="L'image sert de miniature si la page est affichée dans une liste", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image pour la liste'),
        ),
        migrations.AlterField(
            model_name='detailpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text="L'image sert de miniature si la page est affichée dans une liste", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image'),
        ),
    ]
