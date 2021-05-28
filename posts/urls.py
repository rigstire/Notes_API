from django.urls import path
from .views import HomePageView, NotesBodyView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('notes/<int:pk>/',NotesBodyView.as_view(),name='notes_detail'),
]