from django.db import models
from django.contrib.auth.models import User
from readers.models import Profile

class Articles(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    title_pic = models.ImageField(upload_to='articles/images/')
    art_text = models.TextField()
    rating = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    feedback = models.TextField()
    commentator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)



    def __str__(self):
        return self.feedback
