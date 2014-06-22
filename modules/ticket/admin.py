from django.contrib import admin
from ticket.models import *

class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_on'
	list_filter = ('status',)
	list_display = ('subject', 'description', 'status', 'creator', 'assigned_to', 'created_on')
	search_fields = ['description']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Reply)