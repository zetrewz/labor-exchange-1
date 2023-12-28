from django.urls import path

from account.views import register, user_login, user_logout

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
