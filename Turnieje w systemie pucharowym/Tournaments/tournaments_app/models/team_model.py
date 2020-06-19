from django.db import models
from django.urls import reverse

from .player_model import Player
from .tournament_model import Tournament


class Team(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)

    def get_players(self):
        return Player.objects.filter(team=self.id)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.name}'
