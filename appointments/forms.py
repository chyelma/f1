from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'file',)

from .models import PatientStory

class StoryForm(forms.ModelForm):
    class Meta:
        model = PatientStory
        fields = ['patient_name', 'story_title', 'story_content']