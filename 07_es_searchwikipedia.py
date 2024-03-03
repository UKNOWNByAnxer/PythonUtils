import wikipedia

def buscar_wikipedia(consulta):
    try:
        resultado = wikipedia.summary(consulta, sentences=3)  # Limitamos el resumen a 3 oraciones para mantenerlo breve.
        return resultado
    except wikipedia.exceptions.DisambiguationError as e:
        return f"La consulta '{consulta}' es ambigua. Por favor, intenta ser más específico."

def guardar_en_archivo(resultado):
    with open("info.txt", "w", encoding="utf-8") as file:
        file.write(resultado)
    print("La información ha sido guardada en el archivo 'info.txt'")

def main():
    wikipedia.set_lang('es')  # Establecer el idioma predeterminado a español
    consulta = input("Ingrese el término que desea buscar en Wikipedia: ")
    resultado = buscar_wikipedia(consulta)
    guardar_en_archivo(resultado)

if __name__ == "__main__":
    main()
