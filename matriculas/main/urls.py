from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clients/", views.client, name="new_clients"),
    path("clients/<int:client_id>/", views.client_detail, name="client_detail"),
    path("registrations/", views.registration, name="registration_list"),
    path("registrations/<pk>/delete/", views.PlateDeleteView.as_view()),
    path("registrations/<pk>/update/", views.PlateUpdateView.as_view()),
]