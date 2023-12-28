from django.contrib import admin
from django.contrib.admin import ModelAdmin

from account.models import EmployerProfile


@admin.register(EmployerProfile)
class EmployerProfileAdmin(ModelAdmin):
    list_display = ['user', 'company_name']
    raw_id_fields = ['user']
