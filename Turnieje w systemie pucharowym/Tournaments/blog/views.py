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


class AllPostsView(LoginRequiredMixin, ListView):
    # model = Team

    # def get_context_data(self, **kwargs):
    #     return {'Teams':  Team.objects.all()}
    pass
