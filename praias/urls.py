from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'praias'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('praia/<int:praia_id>/', views.praia_view, name='praia'),

]

