from django.urls import path

from resume.views import user_resume, resume_detail, resume_create, resume_update, resume_delete, user_responses

app_name = 'resume'

urlpatterns = [
    path('list/', user_resume, name='list'),
    path('detail/<int:pk>/', resume_detail, name='detail'),
    path('create/', resume_create, name='create'),
    path('update/<int:pk>/', resume_update, name='update'),
    path('delete/<int:pk>/', resume_delete, name='delete'),
    path('responses/', user_responses, name='responses'),
]
