# Generated by Django 5.1.6 on 2025-03-12 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_themesettings_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themesettings',
            name='color_background',
            field=models.CharField(blank=True, default='#f0f4f8', max_length=7, verbose_name="Couleur d'arrière-plan (en hexadécimal)"),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_dark_text',
            field=models.CharField(blank=True, default='#20223B', max_length=7, verbose_name='Couleur du texte sombre (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_light_text',
            field=models.CharField(blank=True, default='#edf2f7', max_length=7, verbose_name='Couleur du texte clair (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_link_hover',
            field=models.CharField(blank=True, default='#63b3ed', max_length=7, verbose_name='Couleur au survol des liens (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_primary',
            field=models.CharField(blank=True, default='#20223B', max_length=7, verbose_name='Couleur primaire (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_secondary',
            field=models.CharField(blank=True, default='#297a62', max_length=7, verbose_name='Couleur secondaire (en hexadécimal)'),
        ),
        migrations.AlterField(
            model_name='themesettings',
            name='color_section_bg',
            field=models.CharField(blank=True, default='#d7e8ef', max_length=7, verbose_name='Couleur de fond des sections (en hexadécimal)'),
        ),
    ]
