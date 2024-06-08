from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('lista_de_bandas', views.lista_de_bandas_view, name='lista_de_bandas'),
    path('banda/<int:banda_id>/', views.banda_view, name='banda'),


    path('album/<int:album_id>/', views.album_view, name='album'),
    path('musica/<int:musica_id>/', views.musica_view, name='musica'),
    path('banda/novo', views.nova_banda_view, name="nova_banda"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),
    path('album/novo/<int:banda_id>/', views.novo_album_view,name="novo_album"),

    path('logout/', views.logout_view, name="logout"),

]
