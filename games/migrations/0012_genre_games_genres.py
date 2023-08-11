# Generated by Django 4.2.4 on 2023-08-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_games_studios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='genres',
            field=models.ManyToManyField(to='games.genre'),
        ),
    ]