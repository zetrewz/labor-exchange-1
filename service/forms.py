from django.forms import ModelForm, Form, CharField

from service.models import Resume, Vacancy


class ResumeCreateForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['work_name', 'gender']


class VacancyCreateForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name']


class SearchForm(Form):
    query = CharField()
