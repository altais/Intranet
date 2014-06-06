from string import join
from PIL import Image as PImage
from os.path import join as pjoin

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from intranet.settings import MEDIA_ROOT, MEDIA_URL
from forum.models import *
from forum.forms import *

def main(request):
    categorie = Categorie.objects.all()
    forums = Forum.objects.all()
    return render(request, "forum/list.html", dict(forums=forums, categories=categorie))

def forum(request, pk):
    topic = Topic.objects.filter(forum=pk).order_by("-created")
    forum = Forum.objects.get(pk=pk)
    categorie = Categorie.objects.get(title=forum.Categorie)
    return render(request, "forum/forum.html", dict(topics=topic, pk=pk, forum=forum, categorie=categorie.title))

def topic(request, pk):
    """Listing of posts in a topic."""
    post = Post.objects.filter(topic=pk).order_by("created")
    topic = Topic.objects.get(pk=pk)
    forum = Forum.objects.get(title=topic.forum)
    categorie = Categorie.objects.get(title=forum.Categorie)
    return render(request, "forum/topic.html", dict(posts=post, pk=pk, topic=topic, forum=forum, categorie=categorie.title))
@login_required
def create_topic(request):
    if request.method == 'POST':
        form = New_topic(request.POST)
        if form.is_valid():
            topic = Topic.objects.create(title=form.cleaned_data['title'], creator=request.user, forum=form.cleaned_data['forum'])
            return HttpResponseRedirect(reverse("forum.views.topic", args=[topic.pk]))
           # post = Post.objects.create(topic=topic, body=form.cleaned_data["body"], creator=request.user)
    else: 
        form = New_topic()
    return render(request, 'forum/new_topic.html', locals())

@login_required
def new_post(request):
    p = request.POST
    if p["body"]:
        topic = Topic.objects.get(pk=p["pk"])
        post = Post.objects.create(topic=topic, body=p["body"], creator=request.user)
    return HttpResponseRedirect(reverse("forum.views.topic", args=[topic.pk]))
