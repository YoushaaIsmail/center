# Generated by Django 5.0.6 on 2024-05-17 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0022_alter_news_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comentClinie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Des', models.CharField(max_length=100)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='COclinic_clinic', to='centerapp.clinic')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Coclinic_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ratingClinie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoure', models.FloatField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Raclinic_clinic', to='centerapp.clinic')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Raclinic_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
