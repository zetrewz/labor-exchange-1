from django.contrib import admin
from django.contrib.admin import ModelAdmin

from service.models import Vacancy, Resume, Application


@admin.register(Vacancy)
class VacancyAdmin(ModelAdmin):
    list_display = ['user', 'name']


@admin.register(Resume)
class ResumeAdmin(ModelAdmin):
    list_display = ['user', 'work_name']


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = ['resume', 'vacancy', 'applied']
