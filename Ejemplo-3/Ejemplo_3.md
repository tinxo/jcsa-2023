# Taller - Midiendo la performance de nuestro código - JCSA2023

## Ejemplo 3

Uso de una herramienta para evaluar rendimineto de consultas SQL.

---

En este ejemplo se va a trabajar directamente con la herramienta pgadmin que es la herramienta oficial de admnistración de PostgreSQL.

A partir de un conjunto de contenedores docker disponibles desde el archivo `docker-compose.yml` [fuente](https://github.com/khezen/compose-postgres/tree/master)se van a crear los contenedores necesarios, para eso se tiene que ejecutar el comando:

~~~ bash
    docker-compose up -d
~~~

Una vez instanciados ambos contenedores, se tiene que generar la base de datos **"taller_jcsa"** en el servidor. Eso se puede hacer desde la ui de pgadmin.

Posteriormente, se tiene que realizar la carga de los datos, en este caso se dispone puede hacer mediante el código de la libreta `crear-base.ipynb`.

A partir de ahí se puede utilizar la herramienta para evaluar el rendimiento de las consultas disponibles.
