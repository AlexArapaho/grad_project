from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, PostFeedback, User
from .forms import PostFeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    arts = Articles.objects.all()
    prof = request.user
    page = request.GET.get('page')
    results = 5
    paginator = Paginator(arts, results)
    try:
        arts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        arts = paginator.page(page)
    except EmptyPage:
        page = paginator.page(page)
    return render(request, 'articles/index.html', {'arts': arts, "prof": prof, 'paginator': paginator})


def detail(request, pk):
    # art = get_object_or_404(Articles, pk=art_id)
    art = Articles.objects.get(id=pk)
    form = PostFeedbackForm()
    if request.method == 'POST':
        try:
            form = PostFeedbackForm(request.POST)
            feedback = form.save(commit=False)
            feedback.article = art
            feedback.commentator = request.user.profile
            feedback.save()
            return redirect('detail', pk=art.id)
        except AttributeError:
            return redirect('login')

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
