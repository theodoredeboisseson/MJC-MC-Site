# Generated by Django 5.1.6 on 2025-03-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_rename_carnon_school_hours_content_footersettings_carnon_school_schedule_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_primary', models.CharField(default='#20223B', help_text='Couleur primaire (en hexadécimal)', max_length=7)),
                ('color_secondary', models.CharField(default='#297a62', help_text='Couleur secondaire (en hexadécimal)', max_length=7)),
                ('color_background', models.CharField(default='#f0f4f8', help_text="Couleur d'arrière-plan (en hexadécimal)", max_length=7)),
                ('color_dark_text', models.CharField(default='#20223B', help_text='Couleur du texte sombre (en hexadécimal)', max_length=7)),
                ('color_light_text', models.CharField(default='#edf2f7', help_text='Couleur du texte clair (en hexadécimal)', max_length=7)),
                ('color_link_hover', models.CharField(default='#63b3ed', help_text='Couleur au survol des liens (en hexadécimal)', max_length=7)),
                ('color_primary_light', models.CharField(default='color-mix(in srgb, var(--color-primary) 80%, white 10%)', help_text='Couleur primaire claire (en hexadécimal)', max_length=50)),
                ('color_section_bg', models.CharField(default='#d7e8ef', help_text='Couleur de fond des sections (en hexadécimal)', max_length=7)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
