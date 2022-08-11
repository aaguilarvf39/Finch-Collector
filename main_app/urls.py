from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('gundams/', views.gundams_index, name='index'),
  path('gundams/<int:gundam_id>/', views.gundams_detail, name='detail'),
  path('gundams/create/', views.GundamCreate.as_view(), name='gundams_create'),
  path('gundams/<int:pk>/update/', views.GundamUpdate.as_view(), name='gundams_update'),
  path('gundams/<int:pk>/delete/', views.GundamDelete.as_view(), name='gundams_delete'),
  path('gundams/<int:gundam_id>/add_repair/', views.add_repair, name='add_repair'),
  path('gundams/<int:gundam_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon'),
  path('gundams/<int:gundam_id>/unassoc_weapon/<int:weapon_id>/', views.unassoc_weapon, name='unassoc_weapon'),
  path('weapons/', views.WeaponList.as_view(), name='weapons_index'),
  path('weapons/<int:pk>/', views.WeaponDetail.as_view(), name='weapons_detail'),
  path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
  path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
  path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
]