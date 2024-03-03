import wikipedia

def search_wikipedia(consulta):
    try:
        resultado = wikipedia.summary(consulta, sentences=3)  # Limitamos el resumen a 3 oraciones para mantenerlo breve.
        return resultado
    except wikipedia.exceptions.DisambiguationError as e:
        return f"The consultation '{consulta}' It is ambiguous. Please try to be more specific."

def save_file(resultado):
    with open("info.txt", "w", encoding="utf-8") as file:
        file.write(resultado)
    print("The information has been saved in the file 'info.txt'")

def main():
    wikipedia.set_lang('en')  # Establish the predetermined to English language
    consulta = input("Engrese the term that means search in Wikipedia: ")
    resultado = search_wikipedia(consulta)
    save_file(resultado)

if __name__ == "__main__":
    main()
