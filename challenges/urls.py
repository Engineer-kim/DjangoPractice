from sys import path_hooks
from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("<int:month>" , views.montly_challenge_by_number),
    path("<str:month>" , views.monthly_challenge , name="monthly_challenge"),
]