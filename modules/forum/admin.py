from django.contrib import admin
from forum.models import Categorie, Forum, Topic, Post

admin.site.register(Categorie)
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)