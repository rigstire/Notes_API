from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Notes

class HomePageView(ListView):
    template_name = 'home.html'
    model = Notes

class NotesBodyView(DetailView):
    model = Notes
    template_name = 'body.html'

