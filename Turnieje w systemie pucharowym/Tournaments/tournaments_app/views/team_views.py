from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from tournaments_app.models import Team


class AllTeamView(ListView):
    model = Team
    paginate_by = 5

    def get_context_data(self, **kwargs):
        return {'Teams':  Team.objects.all()}


class DetailTeamView(DetailView):
    model = Team


class CreateTeamView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Team
    login_url = reverse_lazy('login')
    fields = ['name']

    def get_success_url(self):
        return reverse('team-home')


class UpdateTeamView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Team
    fields = ['name']
    login_url = reverse_lazy('login')
    success_message = "Entry was created successfully"

    def get_success_url(self):
        return reverse('team-home')


class DeleteTeamView(LoginRequiredMixin, DeleteView):
    model = Team
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('team-home')
