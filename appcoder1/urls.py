from django.urls import path
from appcoder1 import views


urlpatterns = [
    path("", views.inicio),
    path("", views.estudiantes),
    path("", views.profesores),
    path("", views.cursos),
]