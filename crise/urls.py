from django.urls import path
from . import views

urlpatterns = [
    path('crise/', views.crise, name='crise'),
    path('cadastro_crise/', views.cadastro_crise, name='cadastro_crise'),
    path('deletar_crise/<int:id>/', views.deletar_crise, name='deletar_crise'),
    path('editar_crise/<int:id>/', views.editar_crise, name='editar_crise'),
    
    path('envia_smss', views.envia_smss, name='envia_smss'),
    

    path('contatos/', views.contatos, name='contatos'),
    path('cadastro_contato/', views.cadastro_contato, name='cadastro_contato'),
    path('deletar_contato/<int:id>/', views.deletar_contato, name='deletar_contato'),
    path('editar_contato/<int:id>/', views.editar_contato, name='editar_contato'),
]
