import sqlite3


# Conectar a la base de datos
def conectar():
    return sqlite3.connect("peliculas.db")


# Crear tablas en la base de datos
def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pelicula (
        titulo TEXT,
        año INTEGER,
        duracion INTEGER,
        nombre_estudio TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estrella (
        nombre TEXT,
        direccion TEXT,
        sexo TEXT,
        fecha_nacimiento TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudio (
        nombre TEXT,
        direccion TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Protagoniza (
        titulo_pelicula TEXT,
        año_pelicula INTEGER,
        nombre_estrella TEXT
    )
    """)

    conexion.commit()
    conexion.close()


# Funciones CRUD para Pelicula
def agregar_pelicula(titulo, año, duracion, nombre_estudio):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Pelicula (titulo, año, duracion, nombre_estudio) VALUES (?, ?, ?, ?)",
                   (titulo, año, duracion, nombre_estudio))
    conexion.commit()
    conexion.close()


def eliminar_pelicula(titulo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Pelicula WHERE titulo = ?", (titulo,))
    conexion.commit()
    conexion.close()


def actualizar_pelicula(titulo, nuevo_titulo=None, nuevo_año=None, nueva_duracion=None, nuevo_estudio=None):
    conexion = conectar()
    cursor = conexion.cursor()
    if nuevo_titulo:
        cursor.execute("UPDATE Pelicula SET titulo = ? WHERE titulo = ?", (nuevo_titulo, titulo))
    if nuevo_año:
        cursor.execute("UPDATE Pelicula SET año = ? WHERE titulo = ?", (nuevo_año, titulo))
    if nueva_duracion:
        cursor.execute("UPDATE Pelicula SET duracion = ? WHERE titulo = ?", (nueva_duracion, titulo))
    if nuevo_estudio:
        cursor.execute("UPDATE Pelicula SET nombre_estudio = ? WHERE titulo = ?", (nuevo_estudio, titulo))
    conexion.commit()
    conexion.close()


# Funciones CRUD para Estrella (similares para Estudio y Protagoniza)
def agregar_estrella(nombre, direccion, sexo, fecha_nacimiento):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Estrella (nombre, direccion, sexo, fecha_nacimiento) VALUES (?, ?, ?, ?)",
                   (nombre, direccion, sexo, fecha_nacimiento))
    conexion.commit()
    conexion.close()


def eliminar_estrella(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Estrella WHERE nombre = ?", (nombre,))
    conexion.commit()
    conexion.close()


def actualizar_estrella(nombre, nuevo_nombre=None, nueva_direccion=None, nuevo_sexo=None, nueva_fecha_nacimiento=None):
    conexion = conectar()
    cursor = conexion.cursor()
    if nuevo_nombre:
        cursor.execute("UPDATE Estrella SET nombre = ? WHERE nombre = ?", (nuevo_nombre, nombre))
    if nueva_direccion:
        cursor.execute("UPDATE Estrella SET direccion = ? WHERE nombre = ?", (nueva_direccion, nombre))
    if nuevo_sexo:
        cursor.execute("UPDATE Estrella SET sexo = ? WHERE nombre = ?", (nuevo_sexo, nombre))
    if nueva_fecha_nacimiento:
        cursor.execute("UPDATE Estrella SET fecha_nacimiento = ? WHERE nombre = ?", (nueva_fecha_nacimiento, nombre))
    conexion.commit()
    conexion.close()


# Menú de interacción
def menu():
    crear_tablas()
    while True:
        print("\nGestión de Base de Datos de Películas")
        print("1. Agregar Película")
        print("2. Eliminar Película")
        print("3. Actualizar Película")
        print("4. Agregar Estrella")
        print("5. Eliminar Estrella")
        print("6. Actualizar Estrella")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            año = int(input("Año: "))
            duracion = int(input("Duración: "))
            nombre_estudio = input("Nombre del Estudio: ")
            agregar_pelicula(titulo, año, duracion, nombre_estudio)
            print("Película agregada.")

        elif opcion == "2":
            titulo = input("Título de la Película a eliminar: ")
            eliminar_pelicula(titulo)
            print("Película eliminada.")

        elif opcion == "3":
            titulo = input("Título de la Película a actualizar: ")
            nuevo_titulo = input("Nuevo Título (enter para omitir): ")
            nuevo_año = input("Nuevo Año (enter para omitir): ")
            nueva_duracion = input("Nueva Duración (enter para omitir): ")
            nuevo_estudio = input("Nuevo Estudio (enter para omitir): ")
            actualizar_pelicula(
                titulo,
                nuevo_titulo or None,
                int(nuevo_año) if nuevo_año else None,
                int(nueva_duracion) if nueva_duracion else None,
                nuevo_estudio or None
            )
            print("Película actualizada.")

        elif opcion == "4":
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            sexo = input("Sexo: ")
            fecha_nacimiento = input("Fecha de Nacimiento: ")
            agregar_estrella(nombre, direccion, sexo, fecha_nacimiento)
            print("Estrella agregada.")

        elif opcion == "5":
            nombre = input("Nombre de la Estrella a eliminar: ")
            eliminar_estrella(nombre)
            print("Estrella eliminada.")

        elif opcion == "6":
            nombre = input("Nombre de la Estrella a actualizar: ")
            nuevo_nombre = input("Nuevo Nombre (enter para omitir): ")
            nueva_direccion = input("Nueva Dirección (enter para omitir): ")
            nuevo_sexo = input("Nuevo Sexo (enter para omitir): ")
            nueva_fecha_nacimiento = input("Nueva Fecha de Nacimiento (enter para omitir): ")
            actualizar_estrella(
                nombre,
                nuevo_nombre or None,
                nueva_direccion or None,
                nuevo_sexo or None,
                nueva_fecha_nacimiento or None
            )
            print("Estrella actualizada.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
menu()