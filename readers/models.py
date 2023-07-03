from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='readers/', default='readers/default.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    title = models.CharField(max_length=70)
    feedback = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

