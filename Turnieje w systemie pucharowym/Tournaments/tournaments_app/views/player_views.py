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


class AllPlayerView(LoginRequiredMixin, ListView):
    model = Player

    def get_context_data(self, **kwargs):
        return {'Players':  Player.objects.all()}


class DetailPlayerView(LoginRequiredMixin, DetailView):
    model = Player


class CreatePlayerView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Player
    login_url = 'player_add'
    fields = ['name', 'surname', 'team']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('player-home')


class UpdatePlayerView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Player
    fields = ['name', 'surname', 'team']
    login_url = 'player_update'
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('player_detail')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('player-home')


class DeletePlayerView(LoginRequiredMixin, DeleteView):
    model = Player
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('player-home')
