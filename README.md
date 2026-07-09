# Sistema de Alquiler de Bicicletas

## Integrantes

- Jesús Miranda Arce
- Matías Negretti

## Comisión

Comisión 1

## Descripción general del sistema

Este proyecto corresponde al Trabajo Final Integrador de Laboratorio de Python de la materia Algoritmos y Estructuras de Datos.

El sistema desarrollado permite gestionar el alquiler de bicicletas dentro de un parque o ciudad mediante una aplicación ejecutada por consola. Su objetivo principal es administrar clientes, bicicletas y alquileres, permitiendo registrar nuevos clientes, consultar bicicletas disponibles, iniciar alquileres, finalizar alquileres y calcular automáticamente el tiempo de uso y el importe a pagar.

El sistema también incorpora control del estado de las bicicletas, diferenciando entre bicicletas disponibles, alquiladas y fuera de servicio. Además, permite visualizar estadísticas básicas de utilización, como cantidad de clientes registrados, alquileres realizados, recaudación total, tiempo promedio de uso y bicicleta más utilizada.

El programa fue desarrollado en Python utilizando estructuras condicionales, estructuras repetitivas, funciones, validaciones de datos, acumuladores, contadores y modularización básica.

## Funcionalidades principales

- Registrar clientes.
- Listar clientes registrados.
- Consultar bicicletas disponibles.
- Listar todas las bicicletas y su estado.
- Iniciar un alquiler.
- Finalizar un alquiler.
- Calcular tiempo de uso.
- Calcular importe a pagar.
- Cambiar el estado de una bicicleta.
- Mostrar alquileres realizados.
- Mostrar estadísticas generales del sistema.
- Validar datos ingresados por el usuario.
- Mostrar mensajes de error ante entradas incorrectas.

## Instrucciones de ejecución

Para ejecutar el sistema es necesario tener Python instalado en la computadora.

### Opción 1: ejecutar desde consola

1. Descargar o clonar el repositorio.
2. Abrir una terminal o consola en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main_alquiler_bicicletas.py
```

En algunas computadoras puede ser necesario usar:

```bash
py main_alquiler_bicicletas.py
```

o:

```bash
python3 main_alquiler_bicicletas.py
```

### Opción 2: ejecutar con archivo BAT en Windows

Si el repositorio incluye el archivo `ejecutar_sistema.bat`, se puede iniciar el programa haciendo doble click sobre ese archivo.

Para que funcione correctamente, se recomienda que el archivo `.bat` y el archivo `.py` estén en la misma carpeta:

```text
Sistema_Bicicletas/
│
├── ejecutar_sistema.bat
└── main_alquiler_bicicletas.py
```

## Uso básico del sistema

Al ejecutar el programa se mostrará un menú por consola:

```text
===== SISTEMA DE ALQUILER DE BICICLETAS =====
1. Registrar cliente
2. Listar clientes
3. Listar bicicletas
4. Ver bicicletas disponibles
5. Iniciar alquiler
6. Finalizar alquiler
7. Ver alquileres realizados
8. Ver estadisticas
9. Cambiar estado de bicicleta
0. Salir
```

El usuario debe ingresar el número correspondiente a la opción que desea utilizar.

## Caso de prueba válido

Un ejemplo de ejecución válida sería:

1. Registrar un cliente.
2. Ver bicicletas disponibles.
3. Iniciar un alquiler para el cliente registrado.
4. Finalizar el alquiler ingresando una hora de finalización mayor a la hora de inicio.
5. Consultar las estadísticas del sistema.

Ejemplo:

```text
DNI: 12345678
Nombre: Juan Perez
Telefono: 3794000000
Bicicleta: 1
Hora inicio: 10:00
Hora finalizacion: 11:30
```

Resultado esperado:

- El alquiler se registra correctamente.
- La bicicleta pasa a estado alquilada.
- Al finalizar, la bicicleta vuelve a estar disponible.
- El sistema calcula el tiempo de uso.
- El sistema calcula el importe a pagar.
- Las estadísticas se actualizan.

## Caso con validación o mensaje de error

El sistema contempla validaciones para evitar datos incorrectos.

Ejemplos:

- Ingresar un DNI con letras.
- Ingresar una opción de menú inexistente.
- Intentar alquilar una bicicleta que no existe.
- Intentar alquilar una bicicleta fuera de servicio.
- Intentar finalizar un alquiler inexistente.
- Ingresar una hora de finalización menor o igual a la hora de inicio.

Ejemplo:

```text
Ingrese DNI del cliente: abc
```

Resultado esperado:

```text
Error: el DNI debe contener solo numeros.
```

## Estructura del proyecto

```text
Sistema_Bicicletas/
│
├── main_alquiler_bicicletas.py
├── ejecutar_sistema.bat
└── README.md
```

## Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó asistencia de Inteligencia Artificial como herramienta de apoyo para:

- Organizar la idea general del sistema.
- Proponer una estructura inicial del código.
- Revisar validaciones.
- Mejorar la organización del README.
- Detectar posibles casos de prueba.

Las decisiones finales, la comprensión del funcionamiento del sistema y la revisión del código corresponden a los integrantes del grupo.

## Organización del trabajo en Git

El repositorio debe evidenciar el proceso de construcción del proyecto mediante commits realizados durante el desarrollo. Se recomienda realizar commits separados por avance, por ejemplo:

```text
commit 1: estructura inicial del proyecto
commit 2: agregado de registro de clientes
commit 3: agregado de bicicletas y disponibilidad
commit 4: agregado de inicio y finalizacion de alquileres
commit 5: agregado de calculo de importes
commit 6: agregado de estadisticas
commit 7: agregado de validaciones
commit 8: revision final del README
```
