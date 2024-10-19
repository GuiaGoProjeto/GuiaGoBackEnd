from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('solicitar-redefinicao-senha/', views.solicitar_redefinicao_senha, name='solicitar_redefinicao_senha'),
]