# customuser/urls.py
from django.urls import path

from .views import (
    MyLoginView,
    usersignup, 
    activate_account
)

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', usersignup, name='signup'),
    path(
        'activate/<slug:uidb64>/<slug:token>/',
        activate_account, 
        name='activate'
    )
]