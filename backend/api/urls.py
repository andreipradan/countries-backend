from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.APILogin.as_view()),
    path('register/', views.Register.as_view()),
    path('scores/', views.ScoreList.as_view()),
]
