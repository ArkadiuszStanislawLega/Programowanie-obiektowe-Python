from django.db import models
from django.urls import reverse


class Game(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    date = models.DateField()
    score_a = models.IntegerField(null=True,
                                  blank=True)
    score_b = models.IntegerField(null=True,
                                  blank=True)

    team_a = models.ForeignKey('tournaments_app.Team',
                               related_name='%(class)s_a_team',
                               on_delete=models.DO_NOTHING)

    team_b = models.ForeignKey('tournaments_app.Team',
                               related_name='%(class)s_b_team',
                               on_delete=models.DO_NOTHING)

    group = models.ForeignKey('tournaments_app.Group',
                              on_delete=models.CASCADE)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def get_winner(self):
        if self.score_a > self.score_b:
            return self.team_a
        elif self.score_b > self.score_a:
            return self.team_b

    def __str__(self):
        return f'{self.id} {self.group.round.tournament.name} {self.group.round.name} {self.group.name} {self.date} {self.team_a.name} - {self.team_b.name} '
