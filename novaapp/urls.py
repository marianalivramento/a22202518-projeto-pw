from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('about_me/', views.about_me_view, name='about_me'),
    path('journal_entrances/', views.journal_entrances_view, name='journal_entrances'),
    path('media/', views.media_view, name='media'),
]
