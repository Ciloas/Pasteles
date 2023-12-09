import json

def cargar_datos_desde_json(archivo):
    try:
        with open(archivo, 'r') as file:
            datos = json.load(file)
        return datos
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al cargar {archivo}: {e}")
        return []

def guardar_datos_en_json(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=2)

def cargar_preguntas():
    return cargar_datos_desde_json('ingredientes.json')

def cargar_respuestas_pasteles():
    return cargar_datos_desde_json('recetas.json')

def guardar_respuestas_pasteles(respuestas_pasteles):
    guardar_datos_en_json('recetas.json', respuestas_pasteles)

def mostrar_lista_pasteles(datos_pasteles):
    if not datos_pasteles:
        print("No hay información disponible.")
        return
    print("Lista de Pasteles:")
    for pastel in datos_pasteles:
        nombre = pastel.get('nombre', 'Pastel no disponible')
        requisitos = pastel.get('requisitos', 'Receta no disponibles')
        print(f"{nombre} - Receta: {requisitos}")

def realizar_entrevista(preguntas):
    respuestas_usuario = {}

    print("Bien, primero veamos qué tienes para hacer un pastel\n")
    for i, pregunta in enumerate(preguntas, start=1):
        respuesta = input(f"{pregunta['pregunta']}: ").lower()
        respuestas_usuario[f"P{i}"] = respuesta
    return respuestas_usuario

def encontrar_pasteles_coincidentes(respuestas_usuario, datos_pasteles):
    pasteles_coincidentes = []

    for pastel in datos_pasteles:
        coincidencias = all(
            respuestas_usuario.get(pregunta, '').lower() == pastel["respuestas"].get(pregunta, '').lower()
            for pregunta in respuestas_usuario
        )
        if coincidencias:
            pasteles_coincidentes.append(pastel["nombre"])
    return pasteles_coincidentes

# Cargar datos desde archivos JSON
preguntas = cargar_preguntas()
datos_pasteles = cargar_respuestas_pasteles()

# Inicio
while True:
    print("\n=== Pastelero IA ===")
    print("1- Ver recetas")
    print("2- Qué pastel puedes hacer")
    print("3- Salir")
    opcion = input("Selecciona una opción (1, 2 o 3): ")

    if opcion == '1':
        mostrar_lista_pasteles(datos_pasteles)
    elif opcion == '2':
        respuestas_usuario = realizar_entrevista(preguntas)
        pasteles_coincidentes = encontrar_pasteles_coincidentes(respuestas_usuario, datos_pasteles)
        if pasteles_coincidentes:
            print("Puedes hacerte este pastel:")
            for pastel in pasteles_coincidentes:
                print(pastel)
        else:
            print("No se puede hacer un pastel con esos ingredientes.")
    elif opcion == '3':
        print("¡Vuelve pronto!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Guardar datos actualizados
guardar_respuestas_pasteles(datos_pasteles)
