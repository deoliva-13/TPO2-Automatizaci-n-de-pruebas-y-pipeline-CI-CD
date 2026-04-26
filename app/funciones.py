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

""""
def palabra_mas_larga(texto):
    ""Retorna la palabra más larga del texto. None si está vacío.""
    if not texto or not texto.strip():
        return None
    palabras = texto.split()
    return max(palabras, key=len) 
    
    Se encontraron dos problemas en esta función:
        - Tomaba los puntos y comas como parte de las palabras, lo que no mostraba en realidad la palabra mas larga.
        - No tenía en cuenta que podía haber más de una palabra con la misma cantidad de letras.
"""

def palabra_mas_larga(texto):
    """Retorna una lista con las palabras más largas del texto, ignorando puntuación.
    Si hay empate, devuelve todas las palabras de mayor longitud."""
    if not texto or not texto.strip():
        return None
    import string
    palabras = [p.strip(string.punctuation) for p in texto.split()]
    palabras = [p for p in palabras if p]
    if not palabras:
        return None
    max_len = max(len(p) for p in palabras)
    return [p for p in palabras if len(p) == max_len]


def es_pregunta(texto):
    """Retorna True si el texto es una pregunta."""
    if not texto or not texto.strip():
        return False
    texto = texto.strip()
    return texto.endswith("?") or texto.startswith("¿")


def tiene_numeros(texto):
    """Retorna True si el texto contiene al menos un número."""
    if not texto:
        return False
    return any(c.isdigit() for c in texto)