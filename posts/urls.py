from django.urls import path
from .views import HomePageView, NotesDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView, NotesSearchView, CommentCreateView, CommentDeleteView, CommentUpdateView, complete

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),

    #notes
    path('notes/<int:pk>/',NotesDetailView.as_view(),name='notes_detail'),
    path('post/new/', NotesCreateView.as_view(),name='post_new'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(),name='notes_update'),
    path('notes/<int:pk>/delete/', NotesDeleteView.as_view(),name='notes_delete'),
    path('notes/results/',NotesSearchView.as_view(),name='search_notes'),
    path('<int:pk>/new/',CommentCreateView.as_view(),name='comment_new'),
    path('<int:pk>/delete/',CommentDeleteView.as_view() , name='comment_delete'),
    path('<int:pk>/update/',CommentUpdateView.as_view(), name='comment_update'),
    path('<int:comment_id>/complete', complete, name="complete")
]           