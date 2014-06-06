from django.db import models
from django.contrib.auth.models import User
from string import join

class Categorie(models.Model):
    title = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title

class Forum(models.Model):
    title = models.CharField(max_length=60)
    Categorie = models.ForeignKey(Categorie)
    def __unicode__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title
        
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    topic = models.ForeignKey(Topic)
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return u"%s - %s" % (self.creator, self.topic)
