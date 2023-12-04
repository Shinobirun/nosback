from django.urls import include, path
from .views import UsuarioListView, UsuarioDetailView, PaqueteTuristicoListView, PaqueteTuristicoDetailView, HistorialViajesListView, verificar_email_existente
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'), 
    path('paquetes/', PaqueteTuristicoListView.as_view(), name='paquete-list'),
    path('paquetes/<int:pk>/', PaqueteTuristicoDetailView.as_view(), name='paquete-detail'), 
    path('viajes/', HistorialViajesListView.as_view(), name='viaje-list'),
    path('verificar-email/', verificar_email_existente, name='verificar_email_existente'),
    #path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login')
]

    