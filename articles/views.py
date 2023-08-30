from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, PostFeedback, User, Rating
from .forms import PostFeedbackForm, RatingForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Avg
from django.db.models import Q


def index(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    arts = Articles.objects.filter(Q(art_text__icontains=search_query) | Q(title__icontains=search_query))
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

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    return render(request, 'articles/index.html', {'arts': arts, "prof": prof, 'paginator': paginator,
                                                   'search_query': search_query, 'custom_range': custom_range})


def detail(request, pk):
    # art = get_object_or_404(Articles, pk=art_id)
    art = Articles.objects.get(id=pk)
    qs = art.rating_set.aggregate(Avg("rating"))['rating__avg']
    if qs is not None:
        avg_rating = round(qs, 2)
        art.average_rating = avg_rating
        art.save()
    else:
        avg_rating = 0
    form = PostFeedbackForm()
    form2 = RatingForm()
    if request.method == 'POST':
        try:
            form = PostFeedbackForm(request.POST)
            form2 = RatingForm(request.POST)
            feedback = form.save(commit=False)
            rating = form2.save(commit=False)
            feedback.article = art
            rating.article = art
            feedback.commentator = request.user.profile
            art.average_rating = avg_rating
            feedback.save()
            rating.save()
            return redirect('detail', pk=art.id)
        except AttributeError:
            return redirect('login')


    return render(request, 'articles/details.html', {'art': art, 'form': form, "form2": form2, "avg_rating": avg_rating})
