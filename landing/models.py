from django.db import models

# Create your models here.
class Game(models.Model):
    game_name = models.CharField(max_length=200)
    game_type = models.CharField(max_length=100)

    def __str__(self):
        return self.game_name