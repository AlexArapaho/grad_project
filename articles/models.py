from django.db import models
from django.contrib.auth.models import User
from readers.models import Profile


class Articles(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    title_pic = models.ImageField(upload_to='articles/images/')
    art_text = models.TextField()
    average_rating = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title




class PostFeedback(models.Model):

    feedback = models.TextField()
    commentator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)


    def __str__(self):
        return self.feedback


class Rating(models.Model):
    VOTE = (
        (1, "Отвратительно"),
        (2, "Плохо"),
        (3, "Так себе"),
        (4, "Неплохо"),
        (5, "Отлично!")
    )
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=VOTE, blank=True)

    # def __str__(self):
    #     return self.rating


