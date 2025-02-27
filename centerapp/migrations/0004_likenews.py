# Generated by Django 5.0.4 on 2024-04-19 21:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0003_remove_likedoctor_doctor_remove_likedoctor_patient_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='likenews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likenews_news', to='centerapp.news')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likenews_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
