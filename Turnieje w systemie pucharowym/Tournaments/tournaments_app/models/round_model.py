from django.db import models
from django.urls import reverse
from .group_model import Group


class Round(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    number_of_players = models.IntegerField()
    tournament = models.ForeignKey('tournaments_app.Tournament',
                                   on_delete=models.CASCADE)

    def get_all_groups(self):
        return Group.objects.filter(round_id=self.id)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id}-{self.tournament.name}-{self.name}'
