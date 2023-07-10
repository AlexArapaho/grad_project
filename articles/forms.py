from django.forms import ModelForm
from .models import PostFeedback


class PostFeedbackForm(ModelForm):
    class Meta:
        model = PostFeedback
        fields = ['feedback']

        labels = {
            'feedback': '',
        }