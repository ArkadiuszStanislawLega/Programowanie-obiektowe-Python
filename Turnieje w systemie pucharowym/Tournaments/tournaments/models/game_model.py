from django.db import models
from django.urls import reverse

from .tournament_model import Tournament
from .team_model import Team


class Game(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    score = models.CharField()
    date = models.DateField()
    team_a = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    team_b = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.team_a.name} - {self.team_b.name} wynik: {self.score}'
