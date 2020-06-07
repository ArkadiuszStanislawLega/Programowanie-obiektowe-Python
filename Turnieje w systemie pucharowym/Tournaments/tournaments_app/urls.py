from django.urls import path
from tournaments_app.views import AllTournamentsView, CreateTournamentView, UpdateTournamentView, DetailTournamentView, DeleteTournamentView


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

]
