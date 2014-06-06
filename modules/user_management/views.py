from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def create_account(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			succes = True
	else:
		form = UserCreationForm()
	return render(request,'user/register.html',locals())
