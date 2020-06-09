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


class AllRoundView(LoginRequiredMixin, ListView):
    model = Round

    def get_context_data(self, **kwargs):
        return {'Rounds':  Round.objects.all()}


class DetailRoundView(LoginRequiredMixin, DetailView):
    model = Round


class CreateRoundView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Round
    login_url = 'round_add'
    fields = ['name', 'number_of_players', 'tournament']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('round-home')


class UpdateRoundView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Round
    fields = ['name', 'number_of_players', 'tournament']
    login_url = 'round_update'
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('round_detail')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('round-home')


class DeleteRoundView(LoginRequiredMixin, DeleteView):
    model = Round

    def get_success_url(self):
        return reverse('round-home')
