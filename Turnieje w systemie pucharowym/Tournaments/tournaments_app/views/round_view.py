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

from tournaments_app.models import Round


class AllRoundView(ListView):
    model = Round

    def get_context_data(self, **kwargs):
        return {'Rounds':  Round.objects.all()}


class DetailRoundView(DetailView):
    model = Round


class CreateRoundView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Round
    login_url = reverse_lazy('login')
    fields = ['name', 'number_of_players', 'tournament']

    def get_success_url(self):
        return reverse('round-home')


class UpdateRoundView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Round
    fields = ['name', 'number_of_players', 'tournament']
    login_url = reverse_lazy('login')
    success_message = "Entry was created successfully"

    def get_success_url(self):
        return reverse('round-home')


class DeleteRoundView(LoginRequiredMixin, DeleteView):
    model = Round
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('round-home')
