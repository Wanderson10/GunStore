from django.urls import path
from . import views


urlpatterns = [
    path("weapons/", views.weaponView.as_view()),
    path("weapons/<int:weapon_id>",views.weaponDetailView.as_view()),
    path("weapons/pistols/",views.viewWeaponPistol.as_view()),
    path("weapons/bowls/",views.viewWeaponBow.as_view()),
    path("weapons/crossbowls/",views.viewWeaponCrossbow.as_view()),
    path("weapons/knifes/",views.vieWeaponKnife.as_view()),
    path("weapons/revolvers/",views.vieWeaponRevolver.as_view())
]