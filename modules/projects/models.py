from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    TYPE_CHOICES = (
        ('Projets', 'Projets'),
        ('Examen', 'Examen'),
        ('TD', 'TD'),
        )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    module = models.ForeignKey('Module')
    type = models.CharField(max_length=10,choices=TYPE_CHOICES,default='Projets')
    description = models.CharField(max_length=255)
    subject = models.FileField(null=True, blank=True, upload_to="/var/www/intranet/upload", max_length=100)
    place_available = models.DecimalField(max_digits=4, decimal_places=0)
    start_signup = models.DateTimeField(auto_now=False) 
    end_signup = models.DateTimeField(auto_now=False) 
    start_project = models.DateTimeField(auto_now=False)
    end_project = models.DateTimeField(auto_now=False)
    group_size_min = models.DecimalField(max_digits=1, decimal_places=0)
    group_size_max = models.DecimalField(max_digits=1, decimal_places=0)
    group = models.ManyToManyField('Group', null=True, blank=True, related_name="project_group")
    def __unicode__(self):
		return self.name

class Module(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    place_available = models.DecimalField(max_digits=4, decimal_places=0)
    start_signup = models.DateTimeField(auto_now=False) 
    end_signup = models.DateTimeField(auto_now=False) 
    start_module = models.DateTimeField(auto_now=False)
    end_module = models.DateTimeField(auto_now=False)
    credit = models.DecimalField(max_digits=2, decimal_places=0)
    user = models.ManyToManyField(User, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=2, decimal_places=0)
    user = models.ManyToManyField(User)
    project = models.ForeignKey(Projects,  related_name="group_project")
    def __unicode__(self):
        return self.name