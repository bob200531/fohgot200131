# Generated by Django 4.2.4 on 2023-08-08 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_rename_nameapi_studio_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerapi',
            old_name='name',
            new_name='nameAPI',
        ),
    ]
