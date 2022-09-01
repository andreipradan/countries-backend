from django.urls import path

from .views import APILogin


urlpatterns = [
    path('login', APILogin.as_view()),
]
