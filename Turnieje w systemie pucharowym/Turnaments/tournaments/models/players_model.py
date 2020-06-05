from django.db import models
from django.urls import reverse
from team_model import Team


class Player(models.Model):
    id = models.AutoField(db_index=True, primar_key=True)
    name = models.CharField(max_lenght=20)
    sruname = models.CharField(max_lenght=20)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.name} {self.sruname}'
