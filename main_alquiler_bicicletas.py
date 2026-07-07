# -*- coding: utf-8 -*-
"""
Trabajo Final Integrador - Laboratorio de Python
Sistema de alquiler de bicicletas por consola

Escenario 11: Sistema de alquiler de bicicletas
- Registro de clientes
- Control de bicicletas disponibles / alquiladas / fuera de servicio
- Inicio y finalizacion de alquileres
- Calculo de tiempo de uso
- Calculo de importes
- Estadisticas de utilizacion

El sistema usa listas y diccionarios para guardar datos en memoria.
Al cerrar el programa, los datos cargados durante la ejecucion se pierden.
"""

# =========================
# CONSTANTES DEL SISTEMA
# =========================

TARIFA_POR_MINUTO = 50
ESTADO_DISPONIBLE = "disponible"
ESTADO_ALQUILADA = "alquilada"
ESTADO_FUERA_SERVICIO = "fuera de servicio"


# =========================
# DATOS INICIALES
# =========================

clientes = []

bicicletas = [
    {"id": 1, "tipo": "Urbana", "estado": ESTADO_DISPONIBLE, "usos": 0},
    {"id": 2, "tipo": "Montaña", "estado": ESTADO_DISPONIBLE, "usos": 0},
    {"id": 3, "tipo": "Electrica", "estado": ESTADO_DISPONIBLE, "usos": 0},
    {"id": 4, "tipo": "Infantil", "estado": ESTADO_DISPONIBLE, "usos": 0},
    {"id": 5, "tipo": "Urbana", "estado": ESTADO_FUERA_SERVICIO, "usos": 0},
]

alquileres = []


# =========================
# FUNCIONES DE VALIDACION
# =========================

def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Lee un numero entero desde teclado.
    Valida que sea entero y que este dentro de un rango si se indica.
    """
    while True:
        dato = input(mensaje).strip()

        try:
            numero = int(dato)

            if minimo is not None and numero < minimo:
                print(f"Error: el numero debe ser mayor o igual a {minimo}.")
            elif maximo is not None and numero > maximo:
                print(f"Error: el numero debe ser menor o igual a {maximo}.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un numero entero valido.")


def leer_texto(mensaje):
    """
    Lee texto y evita que el usuario deje el dato vacio.
    """
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el dato no puede quedar vacio.")
        else:
            return texto


def leer_dni():
    """
    Lee y valida un DNI simple.
    Se valida que sea numerico y que tenga entre 7 y 8 digitos.
    """
    while True:
        dni = input("Ingrese DNI del cliente: ").strip()

        if not dni.isdigit():
            print("Error: el DNI debe contener solo numeros.")
        elif len(dni) < 7 or len(dni) > 8:
            print("Error: el DNI debe tener entre 7 y 8 digitos.")
        else:
            return dni


def convertir_hora_a_minutos(hora_texto):
    """
    Convierte una hora en formato HH:MM a minutos.
    Retorna None si el formato no es valido.
    Ejemplo: 10:30 -> 630 minutos.
    """
    partes = hora_texto.split(":")

    if len(partes) != 2:
        return None

    try:
        hora = int(partes[0])
        minuto = int(partes[1])

        if hora < 0 or hora > 23:
            return None

        if minuto < 0 or minuto > 59:
            return None

        return hora * 60 + minuto

    except ValueError:
        return None


def leer_hora(mensaje):
    """
    Lee una hora en formato HH:MM y la convierte a minutos.
    """
    while True:
        hora_texto = input(mensaje).strip()
        minutos = convertir_hora_a_minutos(hora_texto)

        if minutos is None:
            print("Error: ingrese una hora valida con formato HH:MM. Ejemplo: 14:30")
        else:
            return hora_texto, minutos


# =========================
# FUNCIONES DE BUSQUEDA
# =========================

def buscar_cliente_por_dni(dni):
    """
    Busca un cliente por DNI.
    Retorna el diccionario del cliente o None si no existe.
    """
    for cliente in clientes:
        if cliente["dni"] == dni:
            return cliente

    return None


def buscar_bicicleta_por_id(id_bicicleta):
    """
    Busca una bicicleta por ID.
    Retorna el diccionario de la bicicleta o None si no existe.
    """
    for bicicleta in bicicletas:
        if bicicleta["id"] == id_bicicleta:
            return bicicleta

    return None


def buscar_alquiler_activo_por_id(id_alquiler):
    """
    Busca un alquiler activo por ID.
    Retorna el diccionario del alquiler o None si no existe.
    """
    for alquiler in alquileres:
        if alquiler["id_alquiler"] == id_alquiler and alquiler["estado"] == "activo":
            return alquiler

    return None


def cliente_tiene_alquiler_activo(dni):
    """
    Verifica si un cliente ya tiene un alquiler activo.
    """
    for alquiler in alquileres:
        if alquiler["dni_cliente"] == dni and alquiler["estado"] == "activo":
            return True

    return False


def obtener_proximo_id_alquiler():
    """
    Genera el proximo ID de alquiler.
    """
    return len(alquileres) + 1


# =========================
# FUNCIONES DE CLIENTES
# =========================

def registrar_cliente():
    """
    Registra un nuevo cliente validando que el DNI no este repetido.
    """
    print("\n--- REGISTRAR CLIENTE ---")

    dni = leer_dni()

    if buscar_cliente_por_dni(dni) is not None:
        print("Error: ya existe un cliente registrado con ese DNI.")
        return

    nombre = leer_texto("Ingrese nombre y apellido: ")
    telefono = leer_texto("Ingrese telefono: ")

    cliente = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono
    }

    clientes.append(cliente)
    print("Cliente registrado correctamente.")


def listar_clientes():
    """
    Muestra todos los clientes registrados.
    """
    print("\n--- LISTADO DE CLIENTES ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(f"DNI: {cliente['dni']} | Nombre: {cliente['nombre']} | Telefono: {cliente['telefono']}")


# =========================
# FUNCIONES DE BICICLETAS
# =========================

def listar_bicicletas():
    """
    Muestra todas las bicicletas con su estado.
    """
    print("\n--- LISTADO DE BICICLETAS ---")

    for bicicleta in bicicletas:
        print(
            f"ID: {bicicleta['id']} | "
            f"Tipo: {bicicleta['tipo']} | "
            f"Estado: {bicicleta['estado']} | "
            f"Usos: {bicicleta['usos']}"
        )


def listar_bicicletas_disponibles():
    """
    Muestra solamente las bicicletas disponibles.
    """
    print("\n--- BICICLETAS DISPONIBLES ---")

    disponibles = 0

    for bicicleta in bicicletas:
        if bicicleta["estado"] == ESTADO_DISPONIBLE:
            print(f"ID: {bicicleta['id']} | Tipo: {bicicleta['tipo']}")
            disponibles += 1

    if disponibles == 0:
        print("No hay bicicletas disponibles en este momento.")


def cambiar_estado_bicicleta():
    """
    Permite cambiar una bicicleta disponible a fuera de servicio,
    o una bicicleta fuera de servicio a disponible.
    No permite cambiar manualmente una bicicleta alquilada.
    """
    print("\n--- CAMBIAR ESTADO DE BICICLETA ---")
    listar_bicicletas()

    id_bicicleta = leer_entero("Ingrese ID de la bicicleta: ", minimo=1)
    bicicleta = buscar_bicicleta_por_id(id_bicicleta)

    if bicicleta is None:
        print("Error: no existe una bicicleta con ese ID.")
        return

    if bicicleta["estado"] == ESTADO_ALQUILADA:
        print("Error: no se puede cambiar el estado de una bicicleta alquilada.")
        return

    print("\nEstados posibles:")
    print("1. Disponible")
    print("2. Fuera de servicio")

    opcion = leer_entero("Seleccione nuevo estado: ", minimo=1, maximo=2)

    if opcion == 1:
        bicicleta["estado"] = ESTADO_DISPONIBLE
    else:
        bicicleta["estado"] = ESTADO_FUERA_SERVICIO

    print("Estado de bicicleta actualizado correctamente.")


# =========================
# FUNCIONES DE ALQUILERES
# =========================

def iniciar_alquiler():
    """
    Inicia un alquiler:
    - Valida que el cliente exista.
    - Valida que el cliente no tenga otro alquiler activo.
    - Valida que la bicicleta exista y este disponible.
    - Cambia el estado de la bicicleta a alquilada.
    """
    print("\n--- INICIAR ALQUILER ---")

    if len(clientes) == 0:
        print("Error: primero debe registrar al menos un cliente.")
        return

    listar_bicicletas_disponibles()

    dni = leer_dni()
    cliente = buscar_cliente_por_dni(dni)

    if cliente is None:
        print("Error: no existe un cliente registrado con ese DNI.")
        return

    if cliente_tiene_alquiler_activo(dni):
        print("Error: este cliente ya tiene un alquiler activo.")
        return

    id_bicicleta = leer_entero("Ingrese ID de la bicicleta a alquilar: ", minimo=1)
    bicicleta = buscar_bicicleta_por_id(id_bicicleta)

    if bicicleta is None:
        print("Error: no existe una bicicleta con ese ID.")
        return

    if bicicleta["estado"] != ESTADO_DISPONIBLE:
        print("Error: la bicicleta no esta disponible para alquilar.")
        return

    hora_inicio_texto, minutos_inicio = leer_hora("Ingrese hora de inicio (HH:MM): ")

    alquiler = {
        "id_alquiler": obtener_proximo_id_alquiler(),
        "dni_cliente": dni,
        "nombre_cliente": cliente["nombre"],
        "id_bicicleta": id_bicicleta,
        "tipo_bicicleta": bicicleta["tipo"],
        "hora_inicio": hora_inicio_texto,
        "minutos_inicio": minutos_inicio,
        "hora_fin": None,
        "minutos_fin": None,
        "tiempo_uso": None,
        "importe": 0,
        "estado": "activo"
    }

    alquileres.append(alquiler)
    bicicleta["estado"] = ESTADO_ALQUILADA
    bicicleta["usos"] += 1

    print(f"Alquiler iniciado correctamente. ID de alquiler: {alquiler['id_alquiler']}")


def finalizar_alquiler(recaudacion_total, total_alquileres_finalizados, tiempo_total_uso):
    """
    Finaliza un alquiler activo.
    Calcula tiempo de uso e importe.
    Actualiza acumuladores y cambia la bicicleta a disponible.
    Retorna los acumuladores actualizados.
    """
    print("\n--- FINALIZAR ALQUILER ---")

    if len(alquileres) == 0:
        print("No hay alquileres registrados.")
        return recaudacion_total, total_alquileres_finalizados, tiempo_total_uso

    listar_alquileres_activos()

    id_alquiler = leer_entero("Ingrese ID del alquiler a finalizar: ", minimo=1)
    alquiler = buscar_alquiler_activo_por_id(id_alquiler)

    if alquiler is None:
        print("Error: no existe un alquiler activo con ese ID.")
        return recaudacion_total, total_alquileres_finalizados, tiempo_total_uso

    hora_fin_texto, minutos_fin = leer_hora("Ingrese hora de finalizacion (HH:MM): ")

    if minutos_fin <= alquiler["minutos_inicio"]:
        print("Error: la hora de finalizacion debe ser mayor a la hora de inicio.")
        return recaudacion_total, total_alquileres_finalizados, tiempo_total_uso

    tiempo_uso = minutos_fin - alquiler["minutos_inicio"]
    importe = tiempo_uso * TARIFA_POR_MINUTO

    alquiler["hora_fin"] = hora_fin_texto
    alquiler["minutos_fin"] = minutos_fin
    alquiler["tiempo_uso"] = tiempo_uso
    alquiler["importe"] = importe
    alquiler["estado"] = "finalizado"

    bicicleta = buscar_bicicleta_por_id(alquiler["id_bicicleta"])

    if bicicleta is not None:
        bicicleta["estado"] = ESTADO_DISPONIBLE

    recaudacion_total += importe
    total_alquileres_finalizados += 1
    tiempo_total_uso += tiempo_uso

    print("\nAlquiler finalizado correctamente.")
    print(f"Cliente: {alquiler['nombre_cliente']}")
    print(f"Bicicleta: {alquiler['tipo_bicicleta']} - ID {alquiler['id_bicicleta']}")
    print(f"Hora inicio: {alquiler['hora_inicio']}")
    print(f"Hora fin: {alquiler['hora_fin']}")
    print(f"Tiempo de uso: {tiempo_uso} minutos")
    print(f"Importe a pagar: ${importe}")

    return recaudacion_total, total_alquileres_finalizados, tiempo_total_uso


def listar_alquileres():
    """
    Muestra todos los alquileres registrados.
    """
    print("\n--- LISTADO DE ALQUILERES ---")

    if len(alquileres) == 0:
        print("No hay alquileres registrados.")
        return

    for alquiler in alquileres:
        print(
            f"ID alquiler: {alquiler['id_alquiler']} | "
            f"Cliente: {alquiler['nombre_cliente']} | "
            f"DNI: {alquiler['dni_cliente']} | "
            f"Bicicleta ID: {alquiler['id_bicicleta']} | "
            f"Inicio: {alquiler['hora_inicio']} | "
            f"Fin: {alquiler['hora_fin']} | "
            f"Tiempo: {alquiler['tiempo_uso']} | "
            f"Importe: ${alquiler['importe']} | "
            f"Estado: {alquiler['estado']}"
        )


def listar_alquileres_activos():
    """
    Muestra los alquileres que todavia estan activos.
    """
    print("\n--- ALQUILERES ACTIVOS ---")

    activos = 0

    for alquiler in alquileres:
        if alquiler["estado"] == "activo":
            print(
                f"ID alquiler: {alquiler['id_alquiler']} | "
                f"Cliente: {alquiler['nombre_cliente']} | "
                f"Bicicleta ID: {alquiler['id_bicicleta']} | "
                f"Inicio: {alquiler['hora_inicio']}"
            )
            activos += 1

    if activos == 0:
        print("No hay alquileres activos.")


# =========================
# FUNCIONES DE ESTADISTICAS
# =========================

def contar_bicicletas_por_estado(estado):
    """
    Cuenta bicicletas segun su estado.
    """
    contador = 0

    for bicicleta in bicicletas:
        if bicicleta["estado"] == estado:
            contador += 1

    return contador


def obtener_bicicleta_mas_usada():
    """
    Retorna la bicicleta con mayor cantidad de usos.
    Si ninguna fue usada, retorna None.
    """
    bicicleta_mayor = None

    for bicicleta in bicicletas:
        if bicicleta_mayor is None or bicicleta["usos"] > bicicleta_mayor["usos"]:
            bicicleta_mayor = bicicleta

    if bicicleta_mayor is not None and bicicleta_mayor["usos"] > 0:
        return bicicleta_mayor

    return None


def mostrar_estadisticas(recaudacion_total, total_alquileres_finalizados, tiempo_total_uso):
    """
    Muestra estadisticas basicas del sistema.
    """
    print("\n--- ESTADISTICAS DEL SISTEMA ---")

    disponibles = contar_bicicletas_por_estado(ESTADO_DISPONIBLE)
    alquiladas = contar_bicicletas_por_estado(ESTADO_ALQUILADA)
    fuera_servicio = contar_bicicletas_por_estado(ESTADO_FUERA_SERVICIO)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Alquileres registrados: {len(alquileres)}")
    print(f"Alquileres finalizados: {total_alquileres_finalizados}")
    print(f"Recaudacion total: ${recaudacion_total}")
    print(f"Bicicletas disponibles: {disponibles}")
    print(f"Bicicletas alquiladas: {alquiladas}")
    print(f"Bicicletas fuera de servicio: {fuera_servicio}")

    if total_alquileres_finalizados > 0:
        promedio = tiempo_total_uso / total_alquileres_finalizados
        print(f"Tiempo promedio de uso: {promedio:.2f} minutos")
    else:
        print("Tiempo promedio de uso: sin datos")

    bicicleta_mas_usada = obtener_bicicleta_mas_usada()

    if bicicleta_mas_usada is not None:
        print(
            f"Bicicleta mas utilizada: ID {bicicleta_mas_usada['id']} "
            f"({bicicleta_mas_usada['tipo']}) con {bicicleta_mas_usada['usos']} usos"
        )
    else:
        print("Bicicleta mas utilizada: sin datos")


# =========================
# MENU PRINCIPAL
# =========================

def mostrar_menu():
    """
    Muestra el menu principal.
    """
    print("\n======================================")
    print(" SISTEMA DE ALQUILER DE BICICLETAS")
    print("======================================")
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Listar bicicletas")
    print("4. Ver bicicletas disponibles")
    print("5. Iniciar alquiler")
    print("6. Finalizar alquiler")
    print("7. Ver alquileres realizados")
    print("8. Ver estadisticas")
    print("9. Cambiar estado de bicicleta")
    print("0. Salir")


def main():
    """
    Funcion principal del programa.
    Contiene el ciclo repetitivo del menu.
    """
    recaudacion_total = 0
    total_alquileres_finalizados = 0
    tiempo_total_uso = 0

    opcion = -1

    while opcion != 0:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opcion: ", minimo=0, maximo=9)

        if opcion == 1:
            registrar_cliente()

        elif opcion == 2:
            listar_clientes()

        elif opcion == 3:
            listar_bicicletas()

        elif opcion == 4:
            listar_bicicletas_disponibles()

        elif opcion == 5:
            iniciar_alquiler()

        elif opcion == 6:
            recaudacion_total, total_alquileres_finalizados, tiempo_total_uso = finalizar_alquiler(
                recaudacion_total,
                total_alquileres_finalizados,
                tiempo_total_uso
            )

        elif opcion == 7:
            listar_alquileres()

        elif opcion == 8:
            mostrar_estadisticas(
                recaudacion_total,
                total_alquileres_finalizados,
                tiempo_total_uso
            )

        elif opcion == 9:
            cambiar_estado_bicicleta()

        elif opcion == 0:
            print("Saliendo del sistema. Gracias por utilizar el programa.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
