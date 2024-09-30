from django.urls import path
from . import views  # Make sure this line is present and correct

urlpatterns = [
    path('', views.index, name='home'),  # Ensure this path points to views.index
]
