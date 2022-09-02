from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.APILogin.as_view()),
    path('register/', views.Register.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
