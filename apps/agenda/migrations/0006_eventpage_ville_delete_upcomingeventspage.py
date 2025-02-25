# Generated by Django 5.1.6 on 2025-02-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_pasteventspage_upcomingeventspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='ville',
            field=models.CharField(choices=[('Mauguio', 'Mauguio'), ('Carnon', 'Carnon'), ('Les deux', 'Mauguio et Carnon')], default='Mauguio', max_length=10),
        ),
        migrations.DeleteModel(
            name='UpcomingEventsPage',
        ),
    ]
