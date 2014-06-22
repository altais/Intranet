from django.shortcuts import render
from django.http import HttpResponseRedirect
from projects.models import *
from django.shortcuts import get_object_or_404, redirect
import datetime

def list_modules(request):
	time = datetime.datetime.now()
	modules_inscrit = Module.objects.filter(user=request.user)
	modules_non_inscrit = Module.objects.exclude(user=request.user)
	return render(request, 'projects/view_modules.html', locals())

def list_projects(request, slug):
	time = datetime.datetime.now()
	module = Module.objects.get(slug=slug)
	place = module.user.count()
	pourcentage = int(place / module.place_available * 100)
	for username in module.user.all():
		if username == request.user:
			inscrit = "True"
	projects = Projects.objects.filter(module=module)
	project_inscrit = []
	project_non_inscrit = []
	for project in projects:
		try:
			group = Group.objects.get(project=project, user=request.user)
			project_inscrit.append(project)
		except Group.DoesNotExist:
			project_non_inscrit.append(project)
	return render(request, 'projects/view_projects.html', locals())

def view_project(request, slug_module, slug_project):
	time = datetime.datetime.now()
	module = Module.objects.get(slug=slug_module)
	project = Projects.objects.get(slug=slug_project)
	groups = Group.objects.filter(project=project.pk)
	place = 0
	for group in groups:
		for username in group.user.all():
			place = place + 1
			if username == request.user:
				inscrit = True		
	return render(request, 'projects/view_details.html', locals())

def inscription(request, type, slug):
	if type == "adduser_module":
		ret = Module.objects.get(slug=slug)
		ret.user.add(request.user)
	if type == "deluser_module":
		ret = Module.objects.get(slug=slug)
		ret.user.remove(request.user)
	if type == "deluser_group":
		project = Projects.objects.get(slug=slug)
		module = Module.objects.get(name=project.module)
		groups = Group.objects.filter(project=project)
		for group in groups:
			group.delete()
			#group.user.remove(request.user)
		return redirect('projects.views.view_project', module.slug, project.slug )
	if type == "adduser_group":
		project = Projects.objects.get(slug=slug)
		module = Module.objects.get(name=project.module)
		group = Group.objects.create(name=request.user, size=1, project=project)
		group.user.add(request.user)
		return redirect('projects.views.view_project', module.slug, project.slug )
	return redirect('projects.views.list_modules')
