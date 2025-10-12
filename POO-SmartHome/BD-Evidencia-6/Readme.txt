Documentación Técnica – Configuración de la Base de Datos

Dejo el link de acceso al onecompliter https://onecompiler.com/mysql/43wm4g2ch

Motor de Base de Datos
El sistema utiliza como motor de base de datos MySQL, seleccionado por su estabilidad, soporte multiplataforma y compatibilidad con múltiples lenguajes de programación, entre ellos Python. MySQL permite una administración eficiente de datos estructurados, relaciones entre entidades, y escalabilidad para proyectos de tipo académico o productivo.

1. Creación de la Base de Datos y Tablas
El primer paso consiste en ejecutar el script denominado create_tables.sql. Este archivo contiene las sentencias SQL necesarias para inicializar la estructura principal del sistema.

Descripción del proceso:
- La primera instrucción dentro del archivo crea la base de datos que almacenará toda la información del sistema.
  Ejemplo:
  CREATE DATABASE smart_home;
  USE smart_home;
- A continuación, el script define todas las tablas y sus relaciones, incluyendo claves primarias, foráneas, y restricciones necesarias para garantizar la integridad referencial de los datos.

Ejecución:
Podés ejecutarlo desde:
- El cliente de MySQL (línea de comandos), o
- Una interfaz gráfica como MySQL Workbench, DBeaver, o phpMyAdmin.

Comando ejemplo:
mysql -u root -p < create_tables.sql

2. Inserción de Datos y Consultas Iniciales
Una vez creada la estructura, se debe ejecutar el archivo insert_and_select.sql, el cual:
- Inserta los datos iniciales requeridos por el sistema (registros base para pruebas o funcionamiento).
- Contiene consultas SELECT de verificación, que permiten comprobar el correcto almacenamiento y las relaciones entre las tablas.

Ejecución:
Desde la terminal de MySQL:
mysql -u root -p smart_home < insert_and_select.sql
O directamente desde el entorno gráfico, abriendo el archivo y ejecutando todas las sentencias.

Consideraciones Finales
- Es importante ejecutar los scripts en orden:
  1. create_tables.sql
  2. insert_and_select.sql
- Verificar que el servidor MySQL esté en ejecución antes de comenzar.
- En caso de error por base de datos existente, puede eliminarse con:
  DROP DATABASE smart_home;
  y volver a ejecutar el script de creación.

Resultado Esperado
Tras completar estos pasos:
- La base de datos smart_home quedará correctamente creada.
- Todas las tablas estarán disponibles con sus relaciones funcionales.
- Los datos iniciales estarán cargados y listos para ser consultados desde la aplicación o scripts Python que interactúan con MySQL.
