from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'heropage'

urlpatterns = [
    path('', views.index_view, name='index'),

]