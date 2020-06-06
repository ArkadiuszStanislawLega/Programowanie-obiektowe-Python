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

from tournaments_app.models import Tournament


def home(request):
    context = {
        'Tournaments':  Tournament.objects.all()
    }
    return render(request, 'tournaments/base.html', context)


class AllTournamentsView(LoginRequiredMixin, ListView):
    model = Tournament
    login_url = reverse_lazy('index')
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        return {'Tournaments':  Tournament.objects.all()}


class DetailTournamentView(LoginRequiredMixin, DetailView):
    model = Tournament
    login_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateTournamentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tournament
    fields = ['name', 'start_date', 'end_date', 'max_number_of_players']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_positions')
    login_url = reverse_lazy('index')


class UpdateTournamentView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tournament
    fields = ['name', 'start_date', 'end_date', 'max_number_of_players']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_positions')
    login_url = reverse_lazy('index')


class DeleteTournamentView(LoginRequiredMixin, DeleteView):
    model = Tournament
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('all_positions')
