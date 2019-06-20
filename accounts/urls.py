from django.urls import path

from .views import *


urlpatterns = [
    path('login', login),
    path('signUp', signUp),
    path('forgotPassword', forgotPassword),
    path('profile', profile),
    path('updateProfile', updateProfile),
    path('logout', logout),
    path('verifyEmail', verifyEmail),
]
