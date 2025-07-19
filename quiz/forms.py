from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'topic', 'description', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'inputs',
                'placeholder': 'Название'
            }),
            'topic': forms.Select(attrs={
                'class': 'inputs',
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'inputs',
                'placeholder': 'Описание'
            }),
        }