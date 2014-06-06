# -*- coding:utf-8 -*-
from django.contrib import admin
from news.models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie')
    date_hierarchy = 'date'
    ordering       = ('date',)
    search_fields  = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre', ), }
    fieldsets = (
       ('Général', {
            'fields': ('titre', 'slug', 'auteur', 'categorie', 'publie')
        }),
        ('Contenu de l\'article', {
           'description': u'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )
    def apercu_contenu(self, article):
        text = article.contenu[0:70]
        if len(article.contenu) > 70:
            return '%s...' % text
        else:
            return text
    apercu_contenu.short_description = u'Contenu'

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)