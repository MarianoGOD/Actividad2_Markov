import random

#DEFINICIÓN DEL MODELO OCULTO DE MARKOV

# Probabilidades Iniciales (Dia 1)
prob_inicial = {'Estresado': 0.3, 'Relajado': 0.7}

# Matriz de Transicion (De un dia para otro)
transicion = {
    'Estresado': {'Estresado': 0.6, 'Relajado': 0.4},
    'Relajado': {'Estresado': 0.2, 'Relajado': 0.8}
}

# Matriz de Emision (Estado oculto a lo que observamos)
emision = {
    'Estresado': {'Poco Café': 0.2, 'Mucho Café': 0.8},
    'Relajado': {'Poco Café': 0.7, 'Mucho Café': 0.3}
}

def elegir_segun_probabilidad(diccionario_probs):
    """Funcion sencilla para elegir una opcion basada en su probabilidad"""
    numero_azar = random.random()
    acumulado = 0.0
    for clave, prob in diccionario_probs.items():
        acumulado += prob
        if numero_azar <= acumulado:
            return clave
    return list(diccionario_probs.keys())[-1]

def ejecutar_simulacion(dias):
    print(f"--- Iniciando simulación HMM por {dias} días ---")
    
    # Determinamos el estado del primer dia
    estado_actual = elegir_segun_probabilidad(prob_inicial)
    
    estados_ocultos = []
    observaciones_visibles = []
    
    for dia in range(1, dias + 1):
        estados_ocultos.append(estado_actual)
        
        # ¿Cuánto cafe toma hoy basado en su estres?
        cafe_hoy = elegir_segun_probabilidad(emision[estado_actual])
        observaciones_visibles.append(cafe_hoy)
        
        print(f"Dia {dia}: Estado Real = [{estado_actual}] Vemos que toma = [{cafe_hoy}]")
        
        # Calculamos como amanecera mañana
        estado_actual = elegir_segun_probabilidad(transicion[estado_actual])
        
    print("\n--- Resumen de la Simulación ---")
    print(f"Días Estresado: {estados_ocultos.count('Estresado')}")
    print(f"Días Relajado: {estados_ocultos.count('Relajado')}")

# Ejecutamos el programa para simular 10 días
if __name__ == "__main__":
    ejecutar_simulacion(10)
    