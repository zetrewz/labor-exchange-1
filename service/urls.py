from django.urls import path

from service.views import feed, search, apply, remove_application, check_application

app_name = 'service'

urlpatterns = [
    path('', feed, name='feed'),
    path('search/', search, name='search'),
    path('apply/<int:pk>/', apply, name='apply'),
    path('check_application/<int:pk>/', check_application, name='check_application'),
    path('remove_application/<int:pk>/', remove_application, name='remove_application'),
]
