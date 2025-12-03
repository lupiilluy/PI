from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.lista_entregas, name='home'),
    path('entrega/editar/<int:id>/', views.editar_entrega, name='editar_entrega'),
    path('rastreamento/', views.rastreamento, name='rastreamento'),
]

def index(request):
    return render(request, 'core/index.html')