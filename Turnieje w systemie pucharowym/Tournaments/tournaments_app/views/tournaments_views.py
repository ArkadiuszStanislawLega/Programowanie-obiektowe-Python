from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404

from tournaments_app.models import Tournament


class AllTournamentsView(LoginRequiredMixin, ListView):
    model = Tournament
    # login_url = reverse_lazy('tournaments-home')
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        return {'Tournaments':  Tournament.objects.all()}


class DetailTournamentView(LoginRequiredMixin, DetailView):
    model = Tournament


class CreateTournamentView(LoginRequiredMixin, CreateView):
    model = Tournament
    login_url = 'tournament_add'
    fields = ['name', 'start_date', 'end_date',
              'max_number_of_players', 'registered_teams']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tournaments-home')


class UpdateTournamentView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Tournament
    fields = ['name', 'start_date', 'end_date',
              'max_number_of_players', 'registered_teams']
    login_url = 'tournament_update'
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('tournament_detail')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tournaments-home')


class DeleteTournamentView(LoginRequiredMixin, DeleteView):
    model = Tournament
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tournaments-home')
