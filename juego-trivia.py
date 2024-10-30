import json
import random

def cargar_preguntas():
    with open('preguntas-trivia.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def jugar_trivia_completa(preguntas):
    puntaje = 0
    total_preguntas = 0

    for categoria, lista_preguntas in preguntas.items():
        if isinstance(lista_preguntas, dict):
            for subcategoria, sublista in lista_preguntas.items():
                for pregunta in sublista:
                    total_preguntas += 1
                    print(f"\nCategoría: {subcategoria}")
                    print(pregunta['pregunta'])
                    respuesta = input("Tu respuesta: ").strip()
                    if respuesta.lower() == pregunta['respuesta'].lower():
                        puntaje += 1
                        print("¡Correcto!")
                    else:
                        print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")
        else:
            for pregunta in lista_preguntas:
                total_preguntas += 1
                print(f"\nCategoría: {categoria}")
                print(pregunta['pregunta'])
                respuesta = input("Tu respuesta: ").strip()
                if respuesta.lower() == pregunta['respuesta'].lower():
                    puntaje += 1
                    print("¡Correcto!")
                else:
                    print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")

    print(f"\nTu puntaje final es: {puntaje} de {total_preguntas} preguntas.")

def jugar_por_categoria(preguntas):
    categorias = list(preguntas.keys())
    while True:
        print("\nElige una categoría:")
        for i, categoria in enumerate(categorias, 1):
            print(f"{i}. {categoria}")
        print(f"{len(categorias) + 1}. Salir")

        opcion = int(input("Selecciona una opción: ")) - 1
        if opcion == len(categorias):
            break
        elif 0 <= opcion < len(categorias):
            categoria_seleccionada = categorias[opcion]
            puntaje = 0
            total_preguntas = 0

            if isinstance(preguntas[categoria_seleccionada], dict):
                for subcategoria, sublista in preguntas[categoria_seleccionada].items():
                    for pregunta in sublista:
                        total_preguntas += 1
                        print(f"\nCategoría: {subcategoria}")
                        print(pregunta['pregunta'])
                        respuesta = input("Tu respuesta: ").strip()
                        if respuesta.lower() == pregunta['respuesta'].lower():
                            puntaje += 1
                            print("¡Correcto!")
                        else:
                            print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")
            else:
                for pregunta in preguntas[categoria_seleccionada]:
                    total_preguntas += 1
                    print(f"\nCategoría: {categoria_seleccionada}")
                    print(pregunta['pregunta'])
                    respuesta = input("Tu respuesta: ").strip()
                    if respuesta.lower() == pregunta['respuesta'].lower():
                        puntaje += 1
                        print("¡Correcto!")
                    else:
                        print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")

            print(f"\nTu puntaje final en {categoria_seleccionada} es: {puntaje} de {total_preguntas} preguntas.")
        else:
            print("Opción no válida. Por favor, selecciona nuevamente.")

def main():
    preguntas = cargar_preguntas()
    
    while True:
        print("\nBienvenido a la Trivia!")
        print("1. Jugar trivia completa")
        print("2. Jugar por categoría")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            jugar_trivia_completa(preguntas)
        elif opcion == '2':
            jugar_por_categoria(preguntas)
        elif opcion == '3':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona nuevamente.")

if __name__ == "__main__":
    main()
