# Generated by Django 5.1.6 on 2025-02-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_pagedacceuil_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagedacceuil',
            name='hero_type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default='image', max_length=10),
        ),
        migrations.AddField(
            model_name='pagedacceuil',
            name='video_url',
            field=models.URLField(blank=True, help_text='URL YouTube de la vidéo (ex: https://www.youtube.com/watch?v=EQ-DKvLQlyQ)'),
        ),
    ]
