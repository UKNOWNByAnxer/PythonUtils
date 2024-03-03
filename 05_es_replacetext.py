import os

def buscar_reemplazar_texto(archivo, texto_buscar, texto_reemplazar):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read()
        
        contenido_modificado = contenido.replace(texto_buscar, texto_reemplazar)
        
        with open(archivo, 'w') as file:
            file.write(contenido_modificado)
        
        print(f"El texto '{texto_buscar}' ha sido reemplazado por '{texto_reemplazar}' en el archivo {archivo}")
    except FileNotFoundError:
        print("El archivo especificado no se encontró.")

def main():
    archivo = input("Ingrese el nombre del archivo en el que desea buscar y reemplazar texto: ")
    if not os.path.isfile(archivo):
        print("El archivo especificado no se encontró.")
        return
    
    texto_buscar = input("Ingrese el texto que desea buscar: ")
    texto_reemplazar = input("Ingrese el texto con el que desea reemplazar: ")

    buscar_reemplazar_texto(archivo, texto_buscar, texto_reemplazar)

if __name__ == "__main__":
    main()
    input('\n')