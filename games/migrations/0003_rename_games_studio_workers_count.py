# Generated by Django 4.2.4 on 2023-08-08 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_studio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studio',
            old_name='games',
            new_name='workers_count',
        ),
    ]
