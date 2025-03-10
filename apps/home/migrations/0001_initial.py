# Generated by Django 5.1.6 on 2025-03-10 10:14

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
            name='PageAcceuil',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Mots-clés spécifiques à cette page séparés par des virgules', max_length=255)),
                ('intro_title', models.CharField(default='Bienvenue à la MJC', max_length=255, verbose_name="Titre d'introduction")),
                ('video_url', models.URLField(blank=True, help_text="Collez l'URL de la vidéo YouTube (format embed)", null=True, verbose_name='URL de la vidéo YouTube')),
                ('flash_message', wagtail.fields.RichTextField(blank=True, help_text="Message spécial à en dessous de la section d'introduction", null=True, verbose_name='Message flash')),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image de fond')),
            ],
            options={
                'verbose_name': "Page d'Accueil",
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='RotatingWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default="de l'Art", max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='rotating_words', to='home.pageacceuil')),
            ],
        ),
    ]
