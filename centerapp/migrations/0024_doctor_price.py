# Generated by Django 5.0.6 on 2024-05-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0023_comentclinie_ratingclinie'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
