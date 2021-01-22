from django.forms import ModelForm
from .models import *

class ResourcesForm(ModelForm):
    class Meta:
        model = Resources
        fields = '__all__'
