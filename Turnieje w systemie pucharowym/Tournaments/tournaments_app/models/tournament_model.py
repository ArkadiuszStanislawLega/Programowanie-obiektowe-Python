from django.db import models
from django.urls import reverse

from .round_model import Round


class Tournament(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    max_number_of_players = models.IntegerField()
    registered_teams = models.ManyToManyField('tournaments_app.Team')

    def get_all_teams(self):
        return self.registered_teams.all()

    def get_all_rounds(self):
        return Round.objects.filter(tournament=self)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.name}'
