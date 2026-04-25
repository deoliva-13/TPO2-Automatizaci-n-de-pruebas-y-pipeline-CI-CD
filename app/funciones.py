def contar_palabras(texto):
    """Retorna la cantidad de palabras en un texto."""
    if not texto or not texto.strip():
        return 0
    return len(texto.split())


def es_palindromo(palabra):
    """Retorna True si la palabra se lee igual al revés."""
    palabra = palabra.lower().strip()
    return palabra == palabra[::-1]


def contar_vocales(texto):
    """Retorna la cantidad de vocales en un texto."""
    if not texto:
        return 0
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for c in texto if c in vocales)


def contar_oraciones(texto):
    """Retorna la cantidad de oraciones separadas por . ! ?"""
    if not texto:
        return 0
    return sum(1 for c in texto if c in ".!?")


def palabra_mas_larga(texto):
    """Retorna la palabra más larga del texto. None si está vacío."""
    if not texto or not texto.strip():
        return None
    palabras = texto.split()
    return max(palabras, key=len)