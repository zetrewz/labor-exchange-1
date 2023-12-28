from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render

from service.models import Application


@login_required
def chat_room(request, application_id):
    application = Application.objects.get(
        id=application_id)
    return render(request, 'chat/room.html',
                  {'application': application})


@login_required
def holl(request):
    try:
        applications = Application.objects.filter(
            resume=request.user.resume)
    except Application.DoesNotExist:
        applications = []
    return render(request, 'chat/holll.html',
                  {'application': applications})
