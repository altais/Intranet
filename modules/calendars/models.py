from django.db import models
                                                                                                                                                                                        
class evenement(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now=False)
    end = models.DateTimeField(auto_now=False)
    url = models.CharField(max_length=255)
    allDay = models.TextField(default=False)
    def __unicode__(self):
		return self.title