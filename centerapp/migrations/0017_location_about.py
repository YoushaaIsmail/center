# Generated by Django 5.0.6 on 2024-05-16 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0016_appointmentclinic_date_appointmentclinic_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('lat', models.CharField(max_length=30)),
                ('long', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(max_length=30)),
                ('youtube', models.CharField(max_length=30)),
                ('Instagram', models.CharField(max_length=30)),
                ('fasebook', models.CharField(max_length=30)),
                ('loction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likenews_patient', to='centerapp.location')),
            ],
        ),
    ]
