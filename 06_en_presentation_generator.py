def generate_presentation_card(name, title, company, corner, telephone, site_web, location, keywords):
    tarjeta = f"""
    **{name}**

    👨‍💼 {title}

    🏢 {company}

    📧 {corner}

    📞 {telephone}

    🌐 {site_web}

    📍 {location}

    🔑 {keywords}
    """
    return tarjeta

def guardar_tarjeta_en_archivo(_Archivo_name, card):
    with open(_Archivo_name, 'w', encoding='utf-8') as file:
        file.write(card)
    print(f"The presentation card has been saved in '{_Archivo_name}'")

def main():
    print("¡Welcome to the presentation card generator!")
    name = input("Enter your name: ")
    title = input("Enter your title: ")
    company = input("Enter your company's name: ")
    corner = input("Enter your email: ")
    telephone = input("Enter your phone number: ")
    site_web = input("Enter your website: ")
    location = input("Enter your location: ")
    keywords = input("Enter keywords related to your area (separated by ','): ")

    card = generate_presentation_card(name, title, company, corner, telephone, site_web, location, keywords)
    print("Here is your presentation card:")
    print(card)

    _Archivo_name = input("Enter the file name to save the presentation card (include the .txt extension): ")
    guardar_tarjeta_en_archivo(_Archivo_name, card)

if __name__ == "__main__":
    main()
