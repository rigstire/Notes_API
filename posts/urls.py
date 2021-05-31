from django.urls import path
from .views import HomePageView, NotesDetailView, NotesCreateView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('notes/<int:pk>/',NotesDetailView.as_view(),name='notes_detail'),
    path('post/new/', NotesCreateView.as_view(),name='post_new'),
]