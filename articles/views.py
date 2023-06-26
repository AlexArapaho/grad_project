from django.shortcuts import render, get_object_or_404
from .models import Articles
from django.contrib.auth.forms import UserCreationForm


def index(request):
    arts = Articles.objects.all()
    return render(request, 'articles/index.html', {'arts': arts})


def detail(request, art_id):
    art = get_object_or_404(Articles, pk=art_id)
    return render(request, 'articles/details.html', {'art': art})

def signup(request):
    if request.method == "GET":
        return render(request, 'articles/signup.html', {'form': UserCreationForm()})
