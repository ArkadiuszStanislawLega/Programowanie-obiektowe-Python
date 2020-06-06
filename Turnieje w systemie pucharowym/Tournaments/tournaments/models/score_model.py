from django.db import models
from django.urls import reverse


class Score(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    score = models.IntegerField()
    is_win = models.BooleanField()
    team = models.ForeignKey('tournaments.Team', on_delete=models.DO_NOTHING)
    game = models.ForeignKey('tournaments.Game', on_delete=models.DO_NOTHING)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.team.name} - {self.is_win}'
