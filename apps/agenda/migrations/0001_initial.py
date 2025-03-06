# Generated by Django 5.1.6 on 2025-03-06 14:04

import django.db.models.deletion
import django.utils.timezone
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Comma-separated keywords specific to this page', max_length=255)),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Page Agenda',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PastEventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Comma-separated keywords specific to this page', max_length=255)),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Événements passés',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Comma-separated keywords specific to this page', max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Sous-titre')),
                ('content', wagtail.fields.RichTextField(blank=True, verbose_name='Contenu')),
                ('start_date', models.DateField(default=django.utils.timezone.now, help_text="Date de début de l'événement", verbose_name='Date de début')),
                ('end_date', models.DateField(blank=True, help_text="Date de fin de l'événement (laisser vide si l'événement dure un seul jour)", null=True, verbose_name='Date de fin')),
                ('ville', models.CharField(choices=[('Mauguio', 'Mauguio'), ('Carnon', 'Carnon'), ('Les deux', 'Mauguio et Carnon')], default='Mauguio', max_length=10)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Événement',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
