from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'topic', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }