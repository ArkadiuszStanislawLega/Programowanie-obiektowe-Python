from django.db import models
from django.urls import reverse


class Game(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    date = models.DateField()
    score_a = models.ForeignKey('tournaments.Score',
                                null=True,
                                blank=True,
                                related_name='%(class)s_core_a_team',
                                on_delete=models.DO_NOTHING)
    score_b = models.ForeignKey('tournaments.Score',
                                null=True,
                                blank=True,
                                related_name='%(class)s_score_b_team',
                                on_delete=models.DO_NOTHING)

    team_a = models.ForeignKey('tournaments.Team',
                               related_name='%(class)s_a_team',
                               on_delete=models.DO_NOTHING)

    team_b = models.ForeignKey('tournaments.Team',
                               related_name='%(class)s_b_team',
                               on_delete=models.DO_NOTHING)

    tournament = models.ForeignKey('tournaments.Tournament',
                                   on_delete=models.CASCADE)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.team_a.name} - {self.team_b.name} wynik: {self.score_a} : {self.score_b}'
