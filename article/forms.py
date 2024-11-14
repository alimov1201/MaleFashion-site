from django import forms
from article.models import Comment, Contact, Email

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'leave a comment'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

class EmailField(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Your email'})
        }