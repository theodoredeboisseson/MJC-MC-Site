# Generated by Django 5.1.6 on 2025-03-05 08:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_agendaindexpage_seo_keywords_eventpage_seo_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='date',
        ),
        migrations.AddField(
            model_name='eventpage',
            name='end_date',
            field=models.DateField(blank=True, help_text="Date de fin de l'événement (laisser vide si l'événement dure un seul jour)", null=True, verbose_name='Date de fin'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text="Date de début de l'événement", verbose_name='Date de début'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='ville',
            field=models.CharField(choices=[('Mauguio', 'Mauguio'), ('Carnon', 'Carnon')], default='Mauguio', max_length=10),
        ),
    ]
