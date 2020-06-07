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

from tournaments_app.models import Team


class AllTeamView(LoginRequiredMixin, ListView):
    model = Team
    # login_url = reverse_lazy('tournaments-home')
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        return {'Team':  Team.objects.all()}


class DetailTeamView(LoginRequiredMixin, DetailView):
    model = Team


class CreateTeamView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Team
    login_url = 'Team_add'
    fields = ['Team', 'start_date', 'end_date', 'max_number_of_players']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('Team_detail', args=(self.object.pk))


class UpdateTeamView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Team
    fields = ['name', 'start_date', 'end_date', 'max_number_of_players']
    login_url = 'Team_update'
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('Team_detail')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('Team-home')


class DeleteTeamView(LoginRequiredMixin, DeleteView):
    model = Team
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('Team-home')
