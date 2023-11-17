# Taller - Midiendo la performance de nuestro código - JCSA2023

## Ejemplo 2

Haciendo profiling completo de código Python con la librería Scalene.

---

Existen diferentes profilers para Python. Si bien cada uno tiene sus beneficios y contras, Scalene tiene una serie de características que lo hacen preferible.
Por un lado el profiling se hace tanto a nivel de líneas como de funciones, combina información de CPU y memoria, además de incorporar análisis de GPU.
Para más información se puede acceder al [repositorio](https://github.com/plasma-umass/scalene) de la libreria y a un [video(https://www.youtube.com/watch?v=5iEf-_7mM1k&ab_channel=EmeryBerger)] de referencia.

### Ejecución del ejemplo

Pasos a seguir:

1. En una terminal activar el entorno de conda disponible.
2. Ejecutar la siguiente línea:

    ~~~ bash
        python -m scalene --html --output-file reporte.html ejemplo-2.py
    ~~~

3. Visualizar el archivo .html en un navegador web para analizar los resultados.
