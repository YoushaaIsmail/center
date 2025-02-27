# Generated by Django 5.0.6 on 2024-05-17 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0018_offer_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='sevice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='offer_sevice', to='centerapp.clinic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_Therapist', to='centerapp.therapist'),
        ),
    ]
