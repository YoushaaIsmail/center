# Generated by Django 5.0.4 on 2024-04-19 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0005_news_numbercomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Numbercomment',
        ),
    ]
