from django.contrib import admin
from .models import Notes, Comment

# @admin.register(Notes)
# class NotesAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     pass

class CommentInline(admin.TabularInline): # new
    model = Comment

class NotesAdmin(admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]

admin.site.register(Notes, NotesAdmin)
admin.site.register(Comment)