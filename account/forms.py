from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, CharField, Select, ValidationError


class UserRegistrationForm(ModelForm):
    password = CharField(label='Password',
                         widget=PasswordInput)
    password2 = CharField(label='Repeat password',
                          widget=PasswordInput)
    user_type = CharField(label='User Type', widget=Select(
        choices=[('J', 'Job seeker'), ('E', 'Employer')]))

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'user_type']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Password don\'t match.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError('Email already in use.')
        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
