from django.shortcuts import render

def ticket(request):
	return render(request, 'ticket/ticket.html', locals())
