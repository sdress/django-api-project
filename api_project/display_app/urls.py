from django.urls import path
from . import views

urlpatterns = [
    path('today', views.index, name='index'),
    path('previous', views.previous, name='previous')
]