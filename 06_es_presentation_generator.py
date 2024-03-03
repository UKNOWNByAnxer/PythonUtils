def generar_tarjeta_presentacion(nombre, titulo, empresa, correo, telefono, sitio_web, ubicacion, palabras_clave):
    tarjeta = f"""
    **{nombre}**

    👨‍💼 {titulo}

    🏢 {empresa}

    📧 {correo}

    📞 {telefono}

    🌐 {sitio_web}

    📍 {ubicacion}

    🔑 {palabras_clave}
    """
    return tarjeta

def guardar_tarjeta_en_archivo(nombre_archivo, tarjeta):
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        file.write(tarjeta)
    print(f"La tarjeta de presentación ha sido guardada en '{nombre_archivo}'")

def main():
    print("¡Bienvenido al Generador de Tarjetas de Presentación!")
    nombre = input("Ingrese su nombre: ")
    titulo = input("Ingrese su título: ")
    empresa = input("Ingrese el nombre de su empresa: ")
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    sitio_web = input("Ingrese su sitio web: ")
    ubicacion = input("Ingrese su ubicación: ")
    palabras_clave = input("Ingrese palabras clave relacionadas con su área (separadas por coma): ")

    tarjeta = generar_tarjeta_presentacion(nombre, titulo, empresa, correo, telefono, sitio_web, ubicacion, palabras_clave)
    print("Aquí está su tarjeta de presentación:")
    print(tarjeta)

    nombre_archivo = input("Ingrese el nombre del archivo para guardar la tarjeta de presentación (incluya la extensión .txt): ")
    guardar_tarjeta_en_archivo(nombre_archivo, tarjeta)

if __name__ == "__main__":
    main()
