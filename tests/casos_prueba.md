# Casos de Prueba – Analizador de Texto

## Escenario de prueba

**Aplicación:** Analizador de Texto  
**Contexto:** Una herramienta que recibe strings de texto y aplica distintos análisis lingüísticos básicos. El objetivo es verificar que cada función responda correctamente ante entradas válidas, inválidas y casos límite.

---

## Funciones analizadas

| Función | Descripción |
|---|---|
| `contar_palabras` | Retorna la cantidad de palabras en un texto |
| `es_palindromo` | Retorna True/False si una palabra es palíndromo |
| `contar_vocales` | Retorna la cantidad de vocales en un texto |
| `contar_oraciones` | Retorna la cantidad de oraciones separadas por `.` `!` `?` |
| `palabra_mas_larga` | Retorna la palabra más larga del texto |

---

## Casos de prueba

| # | Función | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| TC01 | `contar_palabras` | ✅ Exitoso | `"Hola mundo cruel"` | `3` |
| TC02 | `contar_palabras` | ❌ Error | `""` (vacío) | `0` |
| TC03 | `contar_palabras` | ⚠️ Borde | `"   "` (solo espacios) | `0` |
| TC04 | `es_palindromo` | ✅ Exitoso | `"oso"` | `True` |
| TC05 | `es_palindromo` | ❌ Error | `"casa"` | `False` |
| TC06 | `es_palindromo` | ⚠️ Borde | `"a"` (un carácter) | `True` |
| TC07 | `contar_vocales` | ✅ Exitoso | `"Hola mundo"` | `4` |
| TC08 | `contar_vocales` | ❌ Error | `"xyz"` | `0` |
| TC09 | `contar_vocales` | ⚠️ Borde | `""` (vacío) | `0` |
| TC10 | `contar_oraciones` | ✅ Exitoso | `"Hola. Cómo estás? Bien!"` | `3` |
| TC11 | `contar_oraciones` | ❌ Error | `"Hola mundo"` (sin puntuación) | `0` |
| TC12 | `contar_oraciones` | ⚠️ Borde | `"..."` (solo puntos) | `3` |
| TC13 | `palabra_mas_larga` | ✅ Exitoso | `"el gato duerme"` | `"duerme"` |
| TC14 | `palabra_mas_larga` | ❌ Error | `""` (vacío) | `None` |
| TC15 | `palabra_mas_larga` | ⚠️ Borde | `"a bb ccc"` | `"ccc"` |

---

## Tipos de caso

- ✅ **Exitoso:** entrada válida y representativa, se espera el resultado correcto normal
- ❌ **Error:** entrada inválida o vacía, se espera que la función lo maneje sin romperse
- ⚠️ **Borde:** entrada en el límite de lo válido, donde el comportamiento puede ser menos obvio