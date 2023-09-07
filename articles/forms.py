from django.forms import ModelForm
from .models import PostFeedback, Rating
from django import forms



class PostFeedbackForm(ModelForm):
    class Meta:
        model = PostFeedback
        fields = ['feedback']

        labels = {
            'feedback': '',
        }

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]
        labels = {"rating": "Оценка"}


class ContactForm(forms.Form):
    frommail = forms.EmailField(label='Email')
    subject = forms.CharField(label='Тема', max_length=255)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        fields = ['frommail', 'subject', 'message']