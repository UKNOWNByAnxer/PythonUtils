def analizador_texto(texto):
    # Conteo de caracteres (incluyendo espacios)
    num_caracteres = len(texto)

    # Conteo de palabras
    palabras = texto.split()
    num_palabras = len(palabras)

    # Conteo de líneas
    lineas = texto.split('\n')
    num_lineas = len(lineas)

    # Conteo de párrafos (separados por líneas en blanco)
    parrafos = texto.split('\n\n')
    num_parrafos = len(parrafos)

    return {
        "Número de caracteres": num_caracteres,
        "Número de palabras": num_palabras,
        "Número de líneas": num_lineas,
        "Número de párrafos": num_parrafos
    }

def main():
    archivo = input("Ingresa el nombre del archivo de texto con extension:\n")
    try:
        with open(archivo, 'r') as file:
            texto = file.read()
        resultado = analizador_texto(texto)
        print("\nAnálisis de texto:")
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")
    except FileNotFoundError:
        print("Archivo no encontrado.")

if __name__ == "__main__":
    main()
    input('\n')