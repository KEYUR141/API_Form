from django.contrib import admin
from django.urls import path
from home.views import FormAPI

urlpatterns = [
    path('form/', FormAPI.as_view()),
]