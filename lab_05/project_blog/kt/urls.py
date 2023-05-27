from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dodaj", views.dodaj),
    path("usun/<int:pk>", views.usun, name="usun"),
    path("edytuj/<int:pk>", views.edytuj, name="edytuj")
]
