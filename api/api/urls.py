from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from medicamentos.views import MedicamentoViewSet

router = routers.DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]