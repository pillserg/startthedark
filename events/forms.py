from django import forms
from startthedark.events.models import Event

class EventForm(forms.ModelForm):
    
    description = forms.CharField(max_length=340, widget=forms.Textarea) 
    class Meta:
        model = Event
        fields = ('description',)
