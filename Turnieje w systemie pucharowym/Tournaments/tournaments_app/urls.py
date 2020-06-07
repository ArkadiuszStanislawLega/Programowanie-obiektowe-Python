from django.urls import path
from tournaments_app.views import *


urlpatterns = [
    path('', AllTournamentsView.as_view(), name="tournaments-home"),

    path('tournaments/add/',
         CreateTournamentView.as_view(),
         name="tournament_add"),

    path('tournaments/<int:pk>/update',
         UpdateTournamentView.as_view(),
         name="tournament_update"),

    path('tournaments/detail/<int:pk>/',
         DetailTournamentView.as_view(),
         name="tournament_detail"),

    path('tournaments/<int:pk>/delete',
         DeleteTournamentView.as_view(),
         name="tournament_delete"),


    path('team/add/',
         CreateTeamView.as_view(),
         name="team_add"),

    path('team/<int:pk>/update',
         UpdateTeamView.as_view(),
         name="team_update"),

    path('team/detail/<int:pk>/',
         DetailTeamView.as_view(),
         name="team_detail"),

    path('team/<int:pk>/delete',
         DeleteTeamView.as_view(),
         name="team_delete"),

]
