from django.shortcuts import render
from projects.models import *

def projects(request):
	modules = Module.objects.all()
	projects = Projects.objects.all()
	group = Group.objects.all()
	return render(request, 'projects/projects.html', locals())
