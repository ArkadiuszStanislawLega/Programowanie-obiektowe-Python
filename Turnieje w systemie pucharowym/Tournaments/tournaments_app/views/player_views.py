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

from tournaments_app.models import Player


class AllPlayerView(ListView):
    model = Player

    def get_context_data(self, **kwargs):
        return {'Players':  Player.objects.all()}


class DetailPlayerView(DetailView):
    model = Player


class CreatePlayerView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Player
    login_url = reverse_lazy('login')
    fields = ['name', 'surname', 'date_of_birth', 'team']

    def get_success_url(self):
        return reverse('player-home')


class UpdatePlayerView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Player
    fields = ['name', 'surname', 'date_of_birth', 'team']
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('player-home')


class DeletePlayerView(LoginRequiredMixin, DeleteView):
    model = Player
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('player-home')
