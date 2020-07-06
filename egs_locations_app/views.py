from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayfieldForm
from .models import Playfield
from django.views.generic import ListView, DetailView

# Home View


# View for all playfields
class PlayfieldView(ListView):
    template_name = 'egs_locations_app/index.html'
    context_object_name = 'playfield_list'

    def get_queryset(self):
        return Playfield.objects.all()
