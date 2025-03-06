# Generated by Django 5.1.6 on 2025-02-27 16:27

import django.db.models.deletion
import modelcluster.fields
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
            name='ActivityList',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Liste des Activités',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ActivityPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Sous-titre')),
                ('content', wagtail.fields.RichTextField(blank=True, verbose_name='Contenu')),
                ('instructors', models.CharField(blank=True, help_text='Nom du/des animateur(s)', max_length=255)),
                ('price_resident', models.DecimalField(decimal_places=2, help_text='Prix pour les résidents Mauguio/Carnon', max_digits=6, null=True)),
                ('price_non_resident', models.DecimalField(decimal_places=2, help_text='Prix pour les non-résidents', max_digits=6, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Activité',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ActivityTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='Ex: Niveau Débutant', max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('days', models.CharField(help_text='Ex: Lundi au Vendredi, ou Mardi/Jeudi', max_length=255)),
                ('activity', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='activites.activitypage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
