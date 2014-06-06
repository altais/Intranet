from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from forum.models import *

class New_topic(ModelForm):
	class Meta:
		model = Topic
		fields = ['title', 'forum']

