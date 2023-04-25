from django.urls import path
from . import views


urlpatterns = [
    path("weapons/", views.weaponView.as_view()),
    path("weapons/<int:weapon_id>",views.weaponDetailView.as_view())
]