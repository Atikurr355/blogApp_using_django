from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:pk>', views.details, name="details"),
]
