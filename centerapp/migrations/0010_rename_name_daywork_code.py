# Generated by Django 5.0.4 on 2024-04-30 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centerapp', '0009_alter_daywork_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daywork',
            old_name='name',
            new_name='code',
        ),
    ]
