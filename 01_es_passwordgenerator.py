import string
import random

def generar_contraseña(longitud, incluir_numeros=True, incluir_minusculas=True, incluir_mayusculas=True, empezar_con_letra=True, incluir_simbolos=True, no_caracteres_similares=True, no_caracteres_duplicados=True, no_caracteres_secuenciales=True):
    caracteres = ''
    if incluir_numeros:
        caracteres += string.digits
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += '!";#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
    if no_caracteres_similares:
        caracteres = caracteres.translate(str.maketrans('', '', 'il1Lo0O'))
    if no_caracteres_duplicados:
        caracteres = ''.join(set(caracteres))
    if no_caracteres_secuenciales:
        caracteres = ''.join([caracteres[i] for i in range(len(caracteres)) if i == 0 or caracteres[i] != caracteres[i-1]])
    
    if empezar_con_letra:
        primer_caracter = random.choice(string.ascii_letters)
    else:
        primer_caracter = random.choice(string.ascii_letters + string.digits + '!";#$%&\'()*+,-./:;<=>?@[]^_`{|}~')
    
    contraseña = primer_caracter + ''.join(random.choices(caracteres, k=longitud-1))
    return contraseña

def obtener_preferencias_usuario():
    longitud = int(input("Longitud de la contraseña: "))
    incluir_numeros = input("Incluir números (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir caracteres en minúscula (s/n): ").lower() == 's'
    incluir_mayusculas = input("Incluir caracteres en mayúscula (s/n): ").lower() == 's'
    empezar_con_letra = input("Empezar con una letra (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos (s/n): ").lower() == 's'
    no_caracteres_similares = input("No usar caracteres similares (s/n): ").lower() == 's'
    no_caracteres_duplicados = input("No usar caracteres duplicados (s/n): ").lower() == 's'
    no_caracteres_secuenciales = input("No usar caracteres secuenciales (s/n): ").lower() == 's'
    return longitud, incluir_numeros, incluir_minusculas, incluir_mayusculas, empezar_con_letra, incluir_simbolos, no_caracteres_similares, no_caracteres_duplicados, no_caracteres_secuenciales

def principal():
    longitud, incluir_numeros, incluir_minusculas, incluir_mayusculas, empezar_con_letra, incluir_simbolos, no_caracteres_similares, no_caracteres_duplicados, no_caracteres_secuenciales = obtener_preferencias_usuario()
    contraseña = generar_contraseña(longitud, incluir_numeros, incluir_minusculas, incluir_mayusculas, empezar_con_letra, incluir_simbolos, no_caracteres_similares, no_caracteres_duplicados, no_caracteres_secuenciales)
    print("Contraseña Generada:", contraseña)

if __name__ == "__main__":
    principal()
    input('\n')