# Smart Home - Hello Worlders

Este proyecto es un ABP perteneciente al módulo Programador I de la Técnicatura en Desarrollo de Software del Instituto Superior Politécnico de Córdoba.

## Funcionalidades (hasta evidencia 6)

- Creación de usuarios
- Consulta de usuarios
- Cambio de rol de usuario
- Agregado de dispositivos
- Consulta de dispositivos
- Gestión de dispositivos

## Estructura del proyecto

```
├── POO-SmartHome
│   ├── BD-Evidencia-5
│   │   ├── create_table.sql
│   │   ├── insert_and_select.sql
│   │   └── Readme.txt
│   ├── BD-Evidencia-6
│   │   ├── create_table.sql
│   │   ├── insert_and_select.sql
│   │   └── Readme.txt
│   ├── conn
│   │   ├── __init__.py
│   │   └── db_conn.py
│   ├── dao
│   │   ├── dispositivos_dao.py
│   │   ├── escenarios_dao.py
│   │   └── usuarios_dao.py
│   ├── Diagrama-Clases
│   │   └── Diagrama de Clases Smart Home - Hello Worlders.pdf
│   ├── domain
│   │   ├── dispositivos.py
│   │   ├── escenarios.py
│   │   └── usuarios.py
│   ├── main.py
│   └── test
│       ├── test_dispositivos_dao.py
│       ├── test_escenarios_dao.py
│       └── test_usuario_dao.py
├── Proyecto funciones (OBSOLETO)
└── README.md
```

Aclaraciones:

- Los archivos que no se utilizan más debido a actualizaciones a través de las evidencias se encuentran marcados como OBSOLETOS en la estructura.
- El diagrama de clases con su respectiva explicación se encuentra en formato PDF en la carpeta Diagrama-Clases.

## Autores

- Sofia Florencia Monje
- Facundo Ariel Faccioli
- Giselda Soledad Mondadori
- Gaston Faustino Alejandro Osess
