from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

def signup(request):
    if request.method == "GET":
        return render(request, 'readers/signup.html', {'form': UserCreationForm()})
