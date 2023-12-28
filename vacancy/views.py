from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET

from service.forms import VacancyCreateForm
from service.models import Vacancy, Application
from service.views import is_employer


@login_required
@require_GET
def user_vacancy_list(request):
    if not is_employer(request.user):
        return redirect('service:feed')
    vacancies = Vacancy.objects.filter(
        user=request.user)
    return render(request, 'vacancy/'
                           'list.html',
                  {'vacancies': vacancies})


@login_required
@require_GET
def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancy/'
                           'detail.html',
                  {'vacancy': vacancy})


@login_required
def vacancy_create(request):
    if not is_employer(request.user):
        return redirect('service:feed')
    form = VacancyCreateForm()

    if request.method == 'POST':
        form = VacancyCreateForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('vacancy:list')

    return render(request, 'vacancy/'
                           'create.html',
                  {'form': form})


@login_required
def vacancy_update(request, pk):
    if not is_employer(request.user):
        return redirect('service:feed')
    vacancy = get_object_or_404(Vacancy, pk=pk)
    form = VacancyCreateForm(instance=vacancy)
    if request.method == 'POST':
        form = VacancyCreateForm(request.POST,
                                 instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy:list')
    return render(request, 'vacancy/'
                           'update.html',
                  {'form': form})


@login_required
def vacancy_delete(request, pk):
    if not is_employer(request.user):
        return redirect('service:feed')
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        vacancy.delete()
        return redirect('vacancy:list')
    return render(request, 'vacancy/'
                           'delete.html',
                  {'vacancy': vacancy})


def vacancy_responses(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    responses = Application.objects.filter(vacancy=vacancy)
    return render(request, 'vacancy/'
                           'responses.html',
                  {'responses': responses})
