import pytest
from app.funciones import (
    contar_palabras,
    es_palindromo,
    contar_vocales,
    contar_oraciones,
    palabra_mas_larga,
    es_pregunta,
    tiene_numeros
)

# =============================================
# TESTS: contar_palabras
# =============================================

def test_contar_palabras_exitoso():
    """TC01 - Texto normal con múltiples palabras"""
    assert contar_palabras("Hola mundo cruel") == 3

def test_contar_palabras_error():
    """TC02 - Texto vacío"""
    assert contar_palabras("") == 0

def test_contar_palabras_borde():
    """TC03 - Solo espacios"""
    assert contar_palabras("   ") == 0


# =============================================
# TESTS: es_palindromo
# =============================================

def test_es_palindromo_exitoso():
    """TC04 - Palabra que sí es palíndromo"""
    assert es_palindromo("oso") == True

def test_es_palindromo_error():
    """TC05 - Palabra que no es palíndromo"""
    assert es_palindromo("casa") == False

def test_es_palindromo_borde():
    """TC06 - Un solo carácter siempre es palíndromo"""
    assert es_palindromo("a") == True


# =============================================
# TESTS: contar_vocales
# =============================================

def test_contar_vocales_exitoso():
    """TC07 - Texto con vocales normales"""
    assert contar_vocales("Hola mundo") == 4

def test_contar_vocales_error():
    """TC08 - Texto sin ninguna vocal"""
    assert contar_vocales("xyz") == 0

def test_contar_vocales_borde():
    """TC09 - Texto vacío"""
    assert contar_vocales("") == 0


# =============================================
# TESTS: contar_oraciones
# =============================================

def test_contar_oraciones_exitoso():
    """TC10 - Texto con tres oraciones"""
    assert contar_oraciones("Hola. Cómo estás? Bien!") == 3

def test_contar_oraciones_error():
    """TC11 - Texto sin puntuación"""
    assert contar_oraciones("Hola mundo") == 0

def test_contar_oraciones_borde():
    """TC12 - Solo signos de puntuación"""
    assert contar_oraciones("...") == 3


# =============================================
# TESTS: palabra_mas_larga
# =============================================

def test_palabra_mas_larga_exitoso():
    """TC13 - Texto normal sin empate"""
    assert palabra_mas_larga("el gato duerme") == ["duerme"]

def test_palabra_mas_larga_error():
    """TC14 - Texto vacío devuelve None"""
    assert palabra_mas_larga("") is None

def test_palabra_mas_larga_borde():
    """TC15 - Palabras de longitud creciente"""
    assert palabra_mas_larga("a bb. ccc") == ["ccc"]

def test_palabra_mas_larga_empate():
    """TC - Dos palabras con la misma longitud máxima"""
    assert palabra_mas_larga("mundo estás") == ["mundo", "estás"]


# =============================================
# TESTS: es_pregunta
# =============================================

def test_es_pregunta_exitoso():
    """TC16 - Texto que es una pregunta"""
    assert es_pregunta("¿Cómo estás?") == True

def test_es_pregunta_error():
    """TC17 - Texto que no es una pregunta"""
    assert es_pregunta("Hola mundo.") == False

def test_es_pregunta_borde():
    """TC18 - Solo el signo de pregunta"""
    assert es_pregunta("?") == True


# =============================================
# TESTS: tiene_numeros
# =============================================

def test_tiene_numeros_exitoso():
    """TC19 - Texto con número"""
    assert tiene_numeros("Tengo 3 gatos") == True

def test_tiene_numeros_error():
    """TC20 - Texto sin números"""
    assert tiene_numeros("Hola mundo") == False

def test_tiene_numeros_borde():
    """TC21 - Texto vacío"""
    assert tiene_numeros("") == False