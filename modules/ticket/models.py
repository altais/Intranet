# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

TICKET_STATUS_CHOICES = (
	('Ouvert', 'Ouvert'),
	('En cours', 'En cours'),
	('En attente de réponse', 'En attente de réponse'),
	('Répondu', 'Répondu'),
	('Fermé', 'Fermé'),
)
TICKET_PRIORITY_CHOICES = (
	('Faible', 'Faible'),
	('Moyenne', 'Moyenne'),
	('Haute', 'Haute'),
)
TICKET_SERVICE_CHOICES = (
	('Administration', 'Administration'),
	('Technique', 'Technique'),
	('Autre', 'Autre'),
)

class Ticket(models.Model):
	subject = models.CharField(max_length=200)
	description = models.TextField()
	reply = models.ManyToManyField('Reply', null=True, blank=True)
	priority = models.CharField(max_length=20, choices=TICKET_PRIORITY_CHOICES, default='Moyenne')
	service = models.CharField(max_length=20, choices=TICKET_SERVICE_CHOICES, default='Administration')
	creator = models.ForeignKey(User, related_name="creator")
	assigned_to = models.ForeignKey(User, null=True, blank=True)
	status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='Ouvert')
	created_on = models.DateTimeField('date_created', auto_now_add=True)
	updated_on = models.DateTimeField('date_updated', auto_now=True)

	def name(self):
		return self.description.split('\n', 1)[0]

class Reply(models.Model):
	reply = models.TextField()
	date = models.DateTimeField('date_created', auto_now_add=True)
	user = models.ForeignKey(User)

	def name(self):
		return self.reply.split('\n', 1)[0]
