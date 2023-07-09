from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Feedback, User
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    arts = Articles.objects.all()
    prof = request.user
    return render(request, 'articles/index.html', {'arts': arts, "prof": prof})


def detail(request, pk):
    # art = get_object_or_404(Articles, pk=art_id)
    art = Articles.objects.get(id=pk)
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        feedback = form.save(commit=False)
        feedback.article = art
        feedback.commentator = request.user.profile
        feedback.save()
        return redirect('detail', pk=art.id)

    # new_feed = Feedback.objects.all()
    # prof = request.user
    # context = {
    #     'art': art,
    #     'new_feed': new_feed,
    #     'prof': prof,
    #     'form': FeedbackForm()
    # }
    #
    # if request.method == 'GET':
    #     return render(request, 'articles/details.html', context)
    # else:
    #     form = FeedbackForm(request.POST)
    #     new_feed = form.save(commit=False)
    #     new_feed.user = request.user.profile
    #     new_feed.save()
    #     return render(request, 'articles/details.html', context)
    return render(request, 'articles/details.html', {'art': art, 'form': form})
