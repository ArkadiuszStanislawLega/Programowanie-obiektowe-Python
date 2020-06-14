from django.db import models
from django.urls import reverse

from .game_model import Game


class Group(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    team_a = models.ForeignKey('tournaments_app.Team',
                               related_name='%(class)s_a_team',
                               on_delete=models.DO_NOTHING)

    team_b = models.ForeignKey('tournaments_app.Team',
                               related_name='%(class)s_b_team',
                               on_delete=models.DO_NOTHING)

    winner = models.ForeignKey('tournaments_app.Team',
                               related_name='%(class)s_win_team',
                               on_delete=models.DO_NOTHING,
                               null=True,
                               blank=True)

    round = models.ForeignKey('tournaments_app.Round',
                              on_delete=models.CASCADE)

    def get_all_games(self):
        return Game.objects.filter(group_id=self.id)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id}-{self.round.tournament.name}-{self.name}-{self.team_a.name}-{self.team_b.name} '
