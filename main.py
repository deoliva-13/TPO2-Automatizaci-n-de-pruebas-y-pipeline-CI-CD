from app.funciones import (
    contar_palabras,
    es_palindromo,
    contar_vocales,
    contar_oraciones,
    palabra_mas_larga,
    es_pregunta,
    tiene_numeros
)

if __name__ == "__main__":
    texto = "Hola mundo. Cómo estás? Todo bien!"

    print("=== Analizador de Texto ===")
    print(f"Texto: '{texto}'")
    print(f"Palabras:          {contar_palabras(texto)}")
    print(f"Vocales:           {contar_vocales(texto)}")
    print(f"Oraciones:         {contar_oraciones(texto)}")
    print(f"Palabra más larga: {palabra_mas_larga(texto)}")
    print(f"¿Tiene números?:   {tiene_numeros(texto)}")
    print(f"¿Es pregunta?:     {es_pregunta(texto)}")
    print()
    print("=== Detector de Palíndromos ===")
    for palabra in ["oso", "ana", "casa", "reconocer"]:
        resultado = "✔ palíndromo" if es_palindromo(palabra) else "✘ no es palíndromo"
        print(f"  '{palabra}': {resultado}")
    print()
    print("=== Detector de Preguntas ===")
    for frase in ["¿Cómo estás?", "Hola mundo.", "?", "Todo bien!"]:
        resultado = "✔ es pregunta" if es_pregunta(frase) else "✘ no es pregunta"
        print(f"  '{frase}': {resultado}")