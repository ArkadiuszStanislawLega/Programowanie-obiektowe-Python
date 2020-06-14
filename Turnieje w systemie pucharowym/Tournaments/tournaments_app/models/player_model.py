from django.db import models
from django.urls import reverse


class Player(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    team = models.ForeignKey('tournaments_app.Team',
                             on_delete=models.DO_NOTHING, null=True)

    def get_absolute_urls(self):
        return reverse('postion_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id} {self.name} {self.surname}'
