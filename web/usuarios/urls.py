from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('buscar/', views.buscar_medicamentos, name='buscar_medicamentos'),
    path('agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('eliminar/', views.eliminar_medicamento, name='eliminar_medicamento'),
]