from django.db import models
from django.urls import reverse


class Tournament(models.Model):
    id = models.AutoField(db_index=True, primar_key=True)
    name = models.CharField(max_lenght=20)
    start_date = models.DateField()
    end_date = models.DateField()
    max_number_of_players = models.IntegerField()

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.name}'
