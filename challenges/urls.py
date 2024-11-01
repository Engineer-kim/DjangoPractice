from sys import path_hooks

from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index),
    path("<int:month>" , views.montly_challenge_by_number),
    path("<str:month>" , views.monthly_challenge , name="monthly_challenge"),
]