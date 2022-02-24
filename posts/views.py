from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Notes, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.views.decorators.http import require_http_methods


class HomePageView(ListView):
    template_name = 'notes/home.html'
    model = Notes


# NOTES VIEWS
class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = CommentForm()
        notes = get_object_or_404(Notes, pk=pk)
        comments = notes.comments.all()

        context['notes'] = notes
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        notes = Notes.objects.filter(id=self.kwargs['pk'])[0]
        comments = notes.comments.all()

        context['notes'] = notes
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            comment = form.cleaned_data['comment']

            comment = Comment.objects.create(
                comment=comment, root_note=notes
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)


class NotesCreateView(CreateView):
    model = Notes
    fields = ['folder']
    template_name = 'notes/post_new.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NotesUpdateView(UpdateView):
    model = Notes
    template_name = 'notes/notes_update.html'
    fields = ['title','body']

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notes/notes_delete.html'
    success_url = reverse_lazy('home')

class NotesSearchView(ListView):
    model = Notes
    template_name = 'notes/search_notes.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Notes.objects.filter(
            Q(folder__icontains=query) | Q(comments__icontains=query)
        )



class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment']
    template_name = 'comment/comment_new.html'

    def form_valid(self,form):
        form.instance.root_note = Notes.objects.get(pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        notes_id = self.object.root_note.pk
        return reverse_lazy('notes_detail', kwargs={'pk':notes_id})

    

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment/comment_delete.html'
    success_url = "/notes/notes_pk"

    def get_success_url(self):
        notes_id = self.object.root_note.id
        return reverse_lazy('notes_detail', kwargs={'pk': notes_id})



# @require_http_methods(['POST'])
# def CommentDeleteView(request,comment_id):
#     Comment.objects.filter(id=comment_id).delete()
#     comments = Comment.objects.filter(user=request.user)
#     return render(request,'notes_detail.html',
#         {'comments':comments,
#          'form':CommentForm(),
#          })


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['comment']
    template_name = 'comment/comment_update.html'

    def get_success_url(self):
        notes_id = self.object.root_note.id
        return reverse_lazy('notes_detail', kwargs={'pk': notes_id})

@require_http_methods(['POST'])
def complete(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.done == True:
        comment.done = False
    else:
        comment.done = True
    comment.save()
    comments = Comment.objects.filter(user=request.user)
    return render(request, "notes_detail.html",
            {'done_form':DoneForm(),
            'comments':comments,
    })

