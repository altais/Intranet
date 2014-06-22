from django.forms import ModelForm
from ticket.models import *

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ['subject', 'description', 'priority', 'service']