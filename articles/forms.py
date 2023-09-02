from django.forms import ModelForm
from .models import PostFeedback, Rating



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


