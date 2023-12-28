from django.urls import path

from vacancy.views import user_vacancy_list, vacancy_detail, vacancy_create, vacancy_update, vacancy_delete, \
    vacancy_responses

app_name = 'vacancy'

urlpatterns = [
    path('list/', user_vacancy_list, name='list'),
    path('detail/<int:pk>/', vacancy_detail, name='detail'),
    path('create/', vacancy_create, name='create'),
    path('update/<int:pk>/', vacancy_update, name='update'),
    path('delete/<int:pk>/', vacancy_delete, name='delete'),
    path('responses/<int:pk>/', vacancy_responses, name='responses'),
]
