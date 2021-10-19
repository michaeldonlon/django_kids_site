# customuser/urls.py
from django.urls import path

from .views import (
    MyLoginView,
    MyPasswordChangeView,
    MyPasswordChangeDoneView,
    MyPasswordResetView,
    MyPasswordResetDoneView,
    MyPasswordResetConfirmView,
    MyPasswordResetCompleteView,
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
    ),
    path('password_change/', 
        MyPasswordChangeView.as_view(), name='password_change'
    ),
    path('password_change/done/', 
        MyPasswordChangeDoneView.as_view(), name='password_change_done'
    ),
    path('password_reset/', 
        MyPasswordResetView.as_view(), name='password_reset'
    ),
    path('password_reset/done/', 
        MyPasswordResetDoneView.as_view(), name='password_reset_done'
    ),
    path('reset/done/', 
        MyPasswordResetCompleteView.as_view(), name='password_reset_complete'
    ),
    path('reset/<uidb64>/<token>/', 
        MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
]
