from django.urls import path

from . import views

app_name = 'presidents'
urlpatterns = [
    path('', views.index, name='index'),
    path('president/<int:president_id>/about', views.about, name='about'),
    path('party/<int:party_id>/', views.party, name='party')
]