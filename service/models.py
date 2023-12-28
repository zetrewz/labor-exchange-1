from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE, DateField, ImageField, IntegerField, CharField, BooleanField, \
    DateTimeField, TextField, OneToOneField, Manager, Index, TextChoices, ManyToManyField
from django.urls import reverse


class PublishedManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Resume(Model):
    class GenderChoices(TextChoices):
        Man = 'M', 'Man'
        Woman = 'W', 'Woman'

    user = OneToOneField(User, on_delete=CASCADE,
                         related_name='resume')
    # first_name = CharField(max_length=100)
    # last_name = CharField(max_length=100)
    work_name = CharField(max_length=100)
    # about = TextField()
    # photo = ImageField(upload_to='users/%Y/%m/%d/',
    #                    blank=True)
    # telephone = IntegerField()
    # city = CharField(max_length=100)
    # citizenship = CharField(max_length=100)
    # salary = IntegerField()
    gender = CharField(max_length=20, choices=GenderChoices.choices)
    # date_of_birth = DateField()
    # experience = TextField()
    created = DateField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('resume:detail',
                       args=[self.id])


class Vacancy(Model):
    user = ForeignKey(User, on_delete=CASCADE,
                      related_name='vacancies')
    name = CharField(max_length=100)
    # about = CharField(max_length=255)
    # responsibilities = CharField(max_length=255)
    # requirements = CharField(max_length=255)
    # conditions = CharField(max_length=255)
    # city = CharField(max_length=100)
    # salary = IntegerField()
    publish = DateField(auto_now=True)
    active = BooleanField(default=True)
    # location = CharField(max_length=255)
    # responses = ManyToManyField(Resume, blank=True,
    #                             related_name='responses')
    objects = Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [Index(fields=['-publish']),
                   Index(fields=['name'])]

    def get_absolute_url(self):
        return reverse('vacancy:detail',
                       args=[self.id])


class Application(Model):
    resume = ForeignKey(Resume, on_delete=CASCADE)
    vacancy = ForeignKey(Vacancy, on_delete=CASCADE)
    applied = BooleanField(default=False)
