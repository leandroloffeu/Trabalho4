from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('criar/', views.criar_evento, name='criar_evento'),
    path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('excluir/<int:evento_id>/', views.excluir_evento, name='excluir_evento'),
]
