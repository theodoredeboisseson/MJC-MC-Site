# Generated by Django 5.1.6 on 2025-03-10 10:14

import django.db.models.deletion
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
            name='BaseIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Mots-clés spécifiques à cette page séparés par des virgules', max_length=255)),
            ],
            options={
                'verbose_name': "Page d'index de base",
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='FlashMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', wagtail.fields.RichTextField(blank=True, help_text="Jusqu'à 100 caractères", null=True)),
                ('show', models.BooleanField(default=False, verbose_name='Montrer')),
            ],
            options={
                'verbose_name': 'Message Flash',
            },
        ),
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_hours_content', wagtail.fields.RichTextField(blank=True, verbose_name='Horaires période scolaire')),
                ('vacation_hours_content', wagtail.fields.RichTextField(blank=True, verbose_name='Horaires période vacances')),
                ('extra', models.CharField(blank=True, max_length=255, verbose_name='Message en extra (optionnel)')),
            ],
            options={
                'verbose_name': 'Informations du Pied de page',
            },
        ),
        migrations.CreateModel(
            name='DetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('seo_keywords', models.CharField(blank=True, help_text='Mots-clés spécifiques à cette page séparés par des virgules', max_length=255)),
                ('content', wagtail.fields.RichTextField(blank=True, verbose_name='Contenu')),
                ('subtitle', models.CharField(blank=True, max_length=250, verbose_name='Sous-titre')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Page de détail',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
