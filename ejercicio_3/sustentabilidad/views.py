from django.shortcuts import render
from .service import obtener_metricas_consumos

# Create your views here.

def vista_panel_sustentabilidad(request):
    registros_consumos = [
        {"Nombre": "Planta A", "ConsumoKwK": 100},
        {"Nombre": "Planta B", "ConsumoKwK": 200},
        {"Nombre": "Planta A", "ConsumoKwK": 150},
        {"Nombre": "Planta C", "ConsumoKwK": 300},
        {"Nombre": "Planta B", "ConsumoKwK": 120},
    ]

    metricas = obtener_metricas_consumos(registros_consumos)

    contexto = {
        "emision_total": metricas["emision_total"],
        "emicionPlantas": metricas["emicionPlantas"],
        "planta_mayor_emicion": metricas["planta_mayor_emicion"],
    }

    return render(request, "sustentabilidad/panel.html", contexto)