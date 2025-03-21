# Generated by Django 5.1.6 on 2025-03-10 10:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agenda', '0001_initial'),
        ('common', '0001_initial'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('detailpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.detailpage')),
                ('start_date', models.DateField(default=django.utils.timezone.now, help_text="Date de début de l'événement", verbose_name='Date de début')),
                ('end_date', models.DateField(blank=True, help_text="Date de fin de l'événement (laisser vide si l'événement dure un seul jour)", null=True, verbose_name='Date de fin')),
                ('ville', models.CharField(choices=[('Mauguio', 'Mauguio'), ('Carnon', 'Carnon'), ('Les deux', 'Mauguio et Carnon')], default='Mauguio', max_length=10)),
            ],
            options={
                'verbose_name': 'Événement',
            },
            bases=('common.detailpage',),
        ),
        migrations.CreateModel(
            name='PastEventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Mots-clés spécifiques à cette page séparés par des virgules', max_length=255)),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Événements passés',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
