from django.forms import ModelForm
from .models import Repairs

class RepairsForm(ModelForm):
  class Meta:
    model = Repairs
    fields = ['date', 'component']
