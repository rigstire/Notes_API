from django.forms import ModelForm
from .models import Notes, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'root_note']

class DoneForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['done']

