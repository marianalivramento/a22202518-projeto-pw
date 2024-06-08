from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('saudacao/<str:nome>', views.saudacao_view),
    path('saudacao/<str:nome>/<int:idade>', views.saudacao_view_2)
]

