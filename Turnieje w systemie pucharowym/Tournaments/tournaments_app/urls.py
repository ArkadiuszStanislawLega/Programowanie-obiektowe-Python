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

    path('team/',
         AllTeamView.as_view(),
         name="team-home"),

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


    path('player/',
         AllPlayerView.as_view(),
         name="player-home"),

    path('player/add/',
         CreatePlayerView.as_view(),
         name="player_add"),

    path('player/<int:pk>/update',
         UpdatePlayerView.as_view(),
         name="player_update"),

    path('player/detail/<int:pk>/',
         DetailPlayerView.as_view(),
         name="player_detail"),

    path('player/<int:pk>/delete',
         DeletePlayerView.as_view(),
         name="player_delete"),

    path('game/',
         AllGameView.as_view(),
         name="game-home"),

    path('game/add/',
         CreateGameView.as_view(),
         name="game_add"),

    path('game/<int:pk>/update',
         UpdateGameView.as_view(),
         name="game_update"),

    path('game/detail/<int:pk>/',
         DetailGameView.as_view(),
         name="game_detail"),

    path('game/<int:pk>/delete',
         DeleteGameView.as_view(),
         name="game_delete"),
]
