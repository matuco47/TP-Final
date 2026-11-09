

def calcular_emisiones_carbono(consumo_kwk, factor_emision = 0.4):
    if consumo_kwk < 0:
        raise ValueError("El consumo de energía no puede ser negativo.")
    return consumo_kwk * factor_emision


def obtener_metricas_consumos(registros):
    emicion_total = 0.0
    emicionPlantas = {}
    planta_mayor_emicion = ("", 0.0) 

    for planta in registros:
        consumo = calcular_emisiones_carbono(planta["ConsumoKwK"])
        emicion_total += consumo
        if planta["Nombre"] not in emicionPlantas:
            emicionPlantas[planta["Nombre"]] = 0.0

        emicionPlantas[planta["Nombre"]] += consumo

        if (emicionPlantas[planta["Nombre"]] > planta_mayor_emicion[1]):
            planta_mayor_emicion = (planta["Nombre"], emicionPlantas[planta["Nombre"]])


    return {
        "emision_total": emicion_total,
        "emicionPlantas": emicionPlantas,
        "planta_mayor_emicion": planta_mayor_emicion
    }