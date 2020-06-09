from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from tournaments_app.models import Game


class AllGameView(LoginRequiredMixin, ListView):
    model = Game

    def get_context_data(self, **kwargs):
        return {'Games':  Game.objects.all()}


class DetailGameView(LoginRequiredMixin, DetailView):
    model = Game


class CreateGameView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Game
    login_url = 'game_add'
    fields = ['date', 'group', 'team_a', 'team_b', 'score_a', 'score_b']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('game-home')


class UpdateGameView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Game
    fields = ['date', 'group', 'team_a', 'team_b', 'score_a', 'score_b']
    login_url = 'game_update'
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('game_detail')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('game-home')


class DeleteGameView(LoginRequiredMixin, DeleteView):
    model = Game

    def get_success_url(self):
        return reverse('game-home')
