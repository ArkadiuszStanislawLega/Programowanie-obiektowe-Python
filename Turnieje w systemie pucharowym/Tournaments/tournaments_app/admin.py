from django.contrib import admin
from .models import Tournament, Game, Player, Score, Team, Group, Round

admin.site.register(Tournament)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(Round)
