from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET

from service.forms import ResumeCreateForm
from service.models import Resume, Application
from service.views import is_worker


@login_required
@require_GET
def user_resume(request):
    if not is_worker(request.user):
        return redirect('service:feed')
    if not Resume.objects.filter(user=request.user).exists():
        return redirect('resume:create')
    resume = Resume.objects.get(user=request.user)
    return render(request, 'resume/list.html',
                  {'resume': resume})


@login_required
@require_GET
def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/'
                           'detail.html',
                  {'resume': resume})


@login_required
def resume_create(request):
    if not is_worker(request.user):
        return redirect('service:feed')
    form = ResumeCreateForm()

    if request.method == 'POST':
        form = ResumeCreateForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('resume:list')

    return render(request, 'resume/'
                           'create.html',
                  {'form': form})


@login_required
def resume_update(request, pk):
    if not is_worker(request.user):
        return redirect('service:feed')
    resume = get_object_or_404(Resume, pk=pk)
    form = ResumeCreateForm(instance=resume)

    if request.method == 'POST':
        form = ResumeCreateForm(request.POST,
                                instance=resume)

        if form.is_valid():
            form.save()
            return redirect('resume:list')

    return render(request, 'resume/'
                           'update.html',
                  {'form': form})


@login_required
def resume_delete(request, pk):
    if not is_worker(request.user):
        return redirect('service:feed')
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume:create')
    return render(request, 'resume/'
                           'delete.html',
                  {'resume': resume})


def user_responses(request):
    if hasattr(request.user, 'resume'):
        responses = Application.objects.filter(
            resume=request.user.resume)
    else:
        responses = []
    return render(request, 'resume/'
                           'responses.html',
                  {'responses': responses})
