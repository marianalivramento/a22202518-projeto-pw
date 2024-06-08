from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'meteo'

urlpatterns = [
    path('', views.lisboa_hoje_view, name='index'),
]
