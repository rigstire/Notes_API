from django.shortcuts import render
# from .forms import NotesForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Notes

class HomePageView(ListView):
    template_name = 'home.html'
    model = Notes

class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes_detail.html'

class NotesCreateView(CreateView):
    model = Notes
    template_name = 'post_new.html'
    fields = ['title','body']
