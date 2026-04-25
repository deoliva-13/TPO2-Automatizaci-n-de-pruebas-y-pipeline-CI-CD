from app.funciones import (
    contar_palabras,
    es_palindromo,
    contar_vocales,
    contar_oraciones,
    palabra_mas_larga
)

if __name__ == "__main__":
    texto = "Hola mundo. Cómo estás? Todo bien!"

    print("=== Analizador de Texto ===")
    print(f"Texto: '{texto}'")
    print(f"Palabras:        {contar_palabras(texto)}")
    print(f"Vocales:         {contar_vocales(texto)}")
    print(f"Oraciones:       {contar_oraciones(texto)}")
    print(f"Palabra más larga: {palabra_mas_larga(texto)}")
    print()
    print("=== Detector de Palíndromos ===")
    for palabra in ["oso", "ana", "casa", "reconocer"]:
        resultado = "✔ palíndromo" if es_palindromo(palabra) else "✘ no es palíndromo"
        print(f"  '{palabra}': {resultado}")