from django.urls import path
from .views import HomePageView, NotesDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('notes/<int:pk>/',NotesDetailView.as_view(),name='notes_detail'),
    path('post/new/', NotesCreateView.as_view(),name='post_new'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(),name='notes_update'),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view(),name='notes_delete')
]