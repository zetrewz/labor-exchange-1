from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from service.forms import SearchForm
from service.models import Vacancy, Resume, Application


def feed(request):
    return render(request, 'base.html')


def is_employer(user):
    return hasattr(user, 'profile')


def is_worker(user):
    return not hasattr(user, 'profile')


@login_required
def search(request):
    query = None
    results = []
    if 'query' in request.GET:

        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            if is_employer(request.user):
                results = (
                    Resume.objects
                    .annotate(rank=SearchRank(SearchVector('work_name'), SearchQuery(query)))
                    .filter(Q(work_name__icontains=query) | Q(work_name__iregex=query))
                    .order_by('-rank'))
            else:
                results = (
                    Vacancy.published
                    .annotate(rank=SearchRank(SearchVector('name'), SearchQuery(query)))
                    .filter(Q(name__icontains=query) | Q(name__iregex=query))
                    .order_by('-rank'))

    return render(request, 'service/search.html',
                  {'query': query,
                   'results': results})


@require_POST
def apply(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    resume = request.user.resume
    user_application, created = Application.objects \
        .get_or_create(resume=resume, vacancy=vacancy)

    if created:
        return JsonResponse({'status': 'applied'})
    else:
        user_application.delete()
        return JsonResponse({'status': 'removed'})


def check_application(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
        resume = request.user.resume
        applied = Application.objects.filter(
            resume=resume, vacancy=vacancy).exists()
        return JsonResponse({'applied': applied})
    except Vacancy.DoesNotExist:
        return JsonResponse({'applied': False})


@require_POST
def remove_application(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    resume = request.user.resume
    application = Application.objects.filter(
        resume=resume, vacancy=vacancy).first()
    if application:
        application.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
