Inventario de Medicamentos (con Django, API REST y Docker)
Proyecto completo que permite gestionar un inventario de medicamentos con control de acceso según tipo de usuario (Administrador o Vendedor).
El sistema incluye una página web, una API REST y dos bases de datos PostgreSQL, todo dockerizado y funcionando en contenedores separados.

Tecnologías utilizadas
Python 3.9
Django
Django REST Framework
PostgreSQL
Docker & Docker Compose

Estructura del proyecto
inventario_farmacia/ ├── api/ # API REST para medicamentos ├── web/ # Aplicación web (login, home, botones) ├── docker-compose.yml # Orquestación de contenedores └── README.md # Documentación del proyecto

Descripción general del funcionamiento
Login en / con usuarios registrados.
Según el rol:
Administrador → puede buscar, agregar y eliminar medicamentos.
Vendedor → solo puede buscar.
La API (api/) expone endpoints para consultar, agregar y eliminar medicamentos.
La web (web/) llama a la API para hacer esas operaciones.
Logout elimina la sesión y regresa al login.

como levantar el proyecto
usa este comando para levantar el proyecto: docker-compose up --build
luego de levantar el proyecto aplicación migracion
docker-compose exec web python manage.py migrate
docker-compose exec api python manage.py migrate
crea el superusuario
docker-compose exec web python manage.py createsuperuser
