#Los microcontroladores de EcoTech Solutions transmiten lecturas térmicas 
# en formato heterogéneo con espacios indeseados, textos mezclados con unidades de 
# medida y atributos incompletos. Se necesita un componente que normalice estos 
# registros individuales y genere un reporte consolidado para la toma de decisiones.
#Punto A: Normalización de Lecturas ( limpiar_registro_sensor ): Diseña la función 
# limpiar_registro_sensor(registro_raw) encargada de procesar un diccionario con 
# datos crudos de un sensor (por ejemplo: {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}).
#  La función debe transformar la información para retornar un nuevo diccionario 
# estandarizado, garantizando que el identificador quede sin espacios sobrantes,
#  la temperatura sea un valor numérico de tipo float sin sufijos de unidad, y la 
# ubicación posea un valor por defecto seguro en caso de no haberse registrado.
#Punto B: Monitoreo y Mapeo Estadístico ( generar_resumen_sensores ): 
# Desarrolla la función generar_resumen_sensores(lista_sensores_limpios, 
# umbral_temperatura) que tome una colección de registros sanitizados previamente 
# con la función del Punto A y un valor límite. Debe retornar una tupla 
# (lista_sensores_alerta, promedio_temperatura) conteniendo los IDs de los 
# dispositivos que superan el umbral estipulado y el promedio térmico global de la 
# planta. Incluye un bloque de ejecución que demuestre el flujo completo desde la 
# limpieza de registros crudos hasta la impresión formateada del reporte final.

def limpiar_registro_sensor(registro_raw: dict[str, str]):
    registro_limpio = []

    for sensor in registro_raw:
        sensor_id = sensor["sensor_id"].strip()
        temperatura_str = sensor["temperatura"].replace("C", "").replace("°C", "").strip()
        temperatura = float(temperatura_str)
        ubicacion = sensor["ubicacion"].strip() if sensor["ubicacion"] else "Zona no registrada"
        registro_limpio.append({
            "sensor_id": sensor_id,
            "temperatura": temperatura,
            "ubicacion": ubicacion})

    return registro_limpio
    

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura: float):
    lista_sensores_alerta = []
    promedio_temperatura = 0.0
    suma_temperaturas = 0.0
    for sensor in lista_sensores_limpios:
        suma_temperaturas += sensor["temperatura"]
        if ( sensor["temperatura"]>= umbral_temperatura):
            lista_sensores_alerta.append(sensor["sensor_id"])
    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)

    print(f"Promedio Temperatura: {promedio_temperatura}°C")
    print("Sensores en alerta:")
    for sensor_id in lista_sensores_alerta:
        print(f" - {sensor_id}")

    return (lista_sensores_alerta , promedio_temperatura)




#Bloque Principal

sensores_raw = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C", 
        "ubicacion": "Planta Norte"
    },
    {
        
        "sensor_id": " SENSOR-002 ",
        "temperatura": "30.2C", 
        "ubicacion": "Planta Sur"
    },
    {
        "sensor_id": " SENSOR-003 ",
        "temperatura": "28.7C", 
        "ubicacion": ""
    },
    {
        "sensor_id": " SENSOR-004 ",
        "temperatura": "35.1C", 
        "ubicacion": "Planta Este"
    },
    {
        "sensor_id": " SENSOR-005 ",
        "temperatura": "22.9C", 
        "ubicacion": None
    }
]

registro_limpio = limpiar_registro_sensor(sensores_raw)

temperatura_umbral = float(input("Ingrese el umbral de temperatura para alerta (30.0): "))

generar_resumen_sensores(registro_limpio, temperatura_umbral)






    

