from django.shortcuts import render
from django.http import HttpResponseRedirect
from projects.models import *
from django.shortcuts import get_object_or_404, redirect
def list_modules(request):
	modules_inscrit = Module.objects.filter(user=request.user)
	modules_non_inscrit = Module.objects.exclude(user=request.user)
	return render(request, 'projects/view_modules.html', locals())

def list_projects(request, slug):
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
	project = Projects.objects.get(slug=slug_project)
	return render(request, 'projects/view_details.html', locals())



def module(request, type, slug):
	if type == "1":
		ret = Module.objects.get(slug=slug)
		ret.user.add(request.user)
	if type == "2":
		ret = Module.objects.get(slug=slug)
		ret.user.remove(request.user)
	return redirect('projects.views.list_modules')
