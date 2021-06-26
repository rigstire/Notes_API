from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views import generic

class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm


# Create your views here.
