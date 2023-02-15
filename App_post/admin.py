from django.contrib import admin
from .models import Task, Post, Like, Comment
# Register your models here.
admin.site.register(Task)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)