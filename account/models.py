from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CharField, TextField, ImageField, CASCADE


class EmployerProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE,
                         related_name='profile')
    # first_name = CharField(max_length=100, blank=True)
    # last_name = CharField(max_length=100, blank=True)
    company_name = CharField(max_length=255, blank=True)
    # about = TextField(blank=True)
    # photo = ImageField(upload_to='users/%Y/%m/%d/',
    #                    blank=True)
