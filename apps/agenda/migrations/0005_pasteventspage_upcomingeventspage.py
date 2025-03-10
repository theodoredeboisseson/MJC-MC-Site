# Generated by Django 5.1.6 on 2025-02-25 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_eventpage_image'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastEventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Événements passés',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='UpcomingEventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Événements à venir',
            },
            bases=('wagtailcore.page',),
        ),
    ]
