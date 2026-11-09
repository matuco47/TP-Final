
from django.urls import path

from ejercicio_3.sustentabilidad.views import vista_panel_sustentabilidad

urlpatterns = [
    path('panel/', vista_panel_sustentabilidad, name='panel_sustentabilidad')
]