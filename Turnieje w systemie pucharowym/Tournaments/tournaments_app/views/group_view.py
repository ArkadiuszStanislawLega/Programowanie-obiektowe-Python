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

from tournaments_app.models import Group


class AllGroupView(ListView):
    model = Group

    def get_context_data(self, **kwargs):
        return {'Groups':  Group.objects.all()}


class DetailGroupView(DetailView):
    model = Group


class CreateGroupView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Group
    login_url = reverse_lazy('login')
    fields = ['name', 'team_a', 'team_b', 'winner', 'round']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('group-home')


class UpdateGroupView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Group
    fields = ['name', 'team_a', 'team_b', 'winner', 'round']
    login_url = reverse_lazy('login')
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('group_detail')

    def get_success_url(self):
        return reverse('group-home')


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Group
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('group-home')
