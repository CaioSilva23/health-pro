from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('cadastro_avaliacao/', views.cadastro_avaliacao, name='cadastro_avaliacao'),
    path('deletar_avaliacao/<int:id>/', views.deletar_avaliacao, name='deletar_avaliacao'),
    path('editar_avaliacao/<int:id>/', views.editar_avaliacao, name='editar_avaliacao'),
]
