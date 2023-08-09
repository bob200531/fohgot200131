from django.db import models
# Create your models here.


class Games(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

class Studio(models.Model):
    name = models.CharField(max_length=255)
    workers_count = models.PositiveIntegerField()
    games_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class PlayerAPI(models.Model):
    nameAPI = models.CharField(max_length=255)
    name_player = models.CharField(max_length=255,default='fohgot')
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nameAPI}'

class git(models.Model):
    pass