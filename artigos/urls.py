from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('artigo/<int:artigo_id>', views.artigo_view, name='artigo'),
    path('autor/<int:autor_id>', views.autor_view, name= 'autor'),
    path('autores/', views.autores_view, name= 'autores'),

    path('review/<int:review_id>', views.review_view, name= 'review'),
    path('utilizador/<int:utilizador_id>', views.utilizador_view, name = 'utilizador'),

    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('register/', views.registo_view, name = "registo"),


    path('artigo/novo', views.novo_artigo_view, name = "novo_artigo"),
    path('artigo/<int:artigo_id>/edita', views.edita_artigo_view, name = "edita_artigo"),

    path('review/<int:review_id>/apaga', views.apaga_review_view, name="apaga_review"),
    path('review/nova', views.nova_review_view,name="nova_review"),


    path('autor/<int:autor_id>/edita', views.edita_autor_view, name="edita_autor"),

]

