from django.db import models
# Create your models here.


class Games(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    studios = models.ManyToManyField('Studio')
    genre = models.ForeignKey(
        to='Genre',       
        on_delete=models.SET_NULL,
        null = True,
        blank = False,
        )

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

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    

class GameCollection(models.Model):
    name =  models.CharField(max_length=100)
    decription =  models.TextField()
    game = models.ManyToManyField(Games,related_name='Коллекция')

    def __str__(self):
        return f'{self.name}'
        


