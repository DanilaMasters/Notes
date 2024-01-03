from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.get_notes, name='notes'),
    path('notes/<int:pk>', views.get_note, name='note'),
]