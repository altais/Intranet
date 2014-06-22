# -*- coding:utf-8 -*-
from django.shortcuts import render
from ticket.models	import *
from ticket.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
def ticket(request):
	tickets = Ticket.objects.filter(creator=request.user)
	return render(request, 'ticket/ticket.html', locals())

def view_ticket(request, id):
	ticket = Ticket.objects.get(id=id)
	return render(request, 'ticket/view_ticket.html', locals())

def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket.objects.create(subject=form.cleaned_data['subject'], description=form.cleaned_data['description'], priority=form.cleaned_data['priority'], service=form.cleaned_data['service'], creator=request.user)
            return HttpResponseRedirect(reverse("ticket.views.view_ticket", args=[ticket.pk]))
    else: 
        form = TicketForm()
    return render(request, 'ticket/new_ticket.html', locals())

def close_ticket(request, id):
     ticket = Ticket.objects.get(id=id)
     ticket.status = "Fermé"
     ticket.save()
     return redirect("ticket.views.ticket")

def new_post(request):
    p = request.POST
    if p["reply"] and p["id"]:
        ticket = Ticket.objects.get(id=p["id"])
        reply = Reply.objects.create(reply=p["reply"], user=request.user)
        ticket.reply.add(reply)
    return HttpResponseRedirect(reverse("ticket.views.view_ticket", args=[ticket.pk]))