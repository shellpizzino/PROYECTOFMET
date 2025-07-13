from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests

# URL base de la API de medicamentos (apuntar al servicio api)
API_URL = 'http://api:8000/medicamentos/'

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def buscar_medicamentos(request):
    resultados = []
    nombre = request.GET.get('nombre')
    if nombre:
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            data = response.json()
            # Filtrar por nombre (case insensitive)
            resultados = [med for med in data if nombre.lower() in med['nombre'].lower()]
        except Exception:
            resultados = []
    return render(request, 'buscar.html', {'resultados': resultados})

@login_required
def agregar_medicamento(request):
    mensaje = ''
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            try:
                response = requests.post(API_URL, json={'nombre': nombre})
                if response.status_code == 201:
                    mensaje = 'Medicamento agregado correctamente.'
                else:
                    mensaje = 'Error al agregar medicamento.'
            except Exception:
                mensaje = 'Error al conectar con la API.'
    return render(request, 'agregar.html', {'mensaje': mensaje})

@login_required
def eliminar_medicamento(request):
    mensaje = ''
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            try:
                get_response = requests.get(API_URL)
                get_response.raise_for_status()
                data = get_response.json()
                med_to_delete = next((med for med in data if med['nombre'].lower() == nombre.lower()), None)
                if med_to_delete:
                    med_id = med_to_delete['id']
                    delete_response = requests.delete(f"{API_URL}{med_id}/")
                    if delete_response.status_code == 204:
                        mensaje = 'Medicamento eliminado correctamente.'
                    else:
                        mensaje = 'Error al eliminar medicamento.'
                else:
                    mensaje = 'Medicamento no encontrado.'
            except Exception:
                mensaje = 'Error al conectar con la API.'
    return render(request, 'eliminar.html', {'mensaje': mensaje})