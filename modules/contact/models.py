from django.db import models
                                                                                                                                                                                        
class Contact(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sujet = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    def __unicode__(self):
		return self.sujet