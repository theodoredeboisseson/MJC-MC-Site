# Generated by Django 5.1.6 on 2025-03-12 10:11

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_alter_themesettings_color_primary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themesettings',
            name='color_background',
            field=colorfield.fields.ColorField(blank=True, default='#f0f4f8', image_field=None, max_length=25, samples=None, verbose_name="Couleur d'arrière-plan (en hexadécimal)"),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_dark_text',
            field=colorfield.fields.ColorField(blank=True, default='#20223B', image_field=None, max_length=25, samples=None, verbose_name='Couleur du texte sombre (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_light_text',
            field=colorfield.fields.ColorField(blank=True, default='#edf2f7', image_field=None, max_length=25, samples=None, verbose_name='Couleur du texte clair (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_link_hover',
            field=colorfield.fields.ColorField(blank=True, default='#63b3ed', image_field=None, max_length=25, samples=None, verbose_name='Couleur au survol des liens (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_primary',
            field=colorfield.fields.ColorField(blank=True, default='#20223B', image_field=None, max_length=25, samples=None, verbose_name='Couleur primaire (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_secondary',
            field=colorfield.fields.ColorField(blank=True, default='#297a62', image_field=None, max_length=25, samples=None, verbose_name='Couleur secondaire (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_section_bg',
            field=colorfield.fields.ColorField(blank=True, default='#d7e8ef', image_field=None, max_length=25, samples=None, verbose_name='Couleur de fond des sections (en hexadécimal)'),
        ),
    ]
