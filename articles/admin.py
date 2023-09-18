from django.contrib import admin
from .models import Articles, PostFeedback, Rating

admin.site.register(Articles)
admin.site.register(PostFeedback)
admin.site.register(Rating)