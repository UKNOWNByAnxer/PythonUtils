import time
import sys

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

def get_conversion_type():
    print_slow("\nSeleccione el tipo de conversión:")
    print_slow("\n1. Temperatura")
    print_slow("\n2. Distancia")
    print_slow("\n3. Masa")
    print_slow("\n4. Velocidad")
    print_slow("\n5. Salida")
    
    while True:
        choice = input("\nIngrese su elección (1-5): ")
        
        if choice in ["1", "2", "3", "4"]:
            return choice
        elif choice == "5":
            return None
        
        print_slow("Elección no válida.Inténtalo de nuevo.")


def get_measurement_unit(conversion_type):
    units = {
        "1": {
            "1": "°C",
            "2": "°F"
        },
        "2": {
            "1": "mm",
            "2": "cm",
            "3": "m",
            "4": "km",
            "5": "pulgada",
            "6": "pies",
            "7": "yardas",
            "8": "milla"
        },
        "3": {
            "1": "mg",
            "2": "g",
            "3": "kg",
            "4": "t",
            "5": "ounce",
            "6": "pounds"
        },
        "4": {
            "1": "m/s",
            "2": "km/h",
            "3": "millas/s",
            "4": "millas/h",
            "5": "nudos"
        }
    }
    
    choices = units[conversion_type]
    
    print_slow(f"\nSelecciona el {conversion_type.lower()} unidad:")
    for i, unit in enumerate(choices.values(), start=1):
        print_slow(f"\n{i}. {unit}")
    print_slow(f"\n{len(choices) + 1}. Devolver")
    
    while True:
        choice = input(f"\nIngrese su elección (1-{len(choices) + 1}): ")
        
        if choice in choices:
            return choices[choice]
        elif choice == str(len(choices) + 1):
            return None
        
        print_slow("Elección no válida. Inténtalo de nuevo.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print_slow("Entrada inválida. Por favor, introduzca un valor numérico.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_distance(distance, from_unit, to_unit):
    conversion_factors = {
        "mm": {"mm": 1, "cm": 0.1, "m": 0.001, "km": 0.000001,
               "pulgada": 0.0393701, "pies": 0.00328084, "yardas": 0.00109361, "milla": 0.000000621371},
        "cm": {"mm": 10, "cm": 1, "m": 0.01, "km": 0.00001,
               "pulgada": 0.393701, "pies": 0.0328084, "yardas": 0.0109361, "milla": 0.00000621371},
        "m": {"mm": 1000, "cm": 100, "m": 1, "km": 0.001,
              "pulgada": 39.3701, "pies": 3.28084, "yardas": 1.09361, "milla": 0.000621371},
        "km": {"mm": 1000000, "cm": 100000, "m": 1000, "km": 1,
               "pulgada": 39370.1, "pies": 3280.84, "yardas": 1093.61, "milla": 0.621371},
        "pulgada": {"mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 0.0000254,
                 "pulgada": 1, "pies": 0.0833333, "yardas": 0.0277778, "milla": 0.0000157828},
        "pies": {"mm": 304.8, "cm": 30.48, "m": 0.3048, "km": 0.0003048,
                 "pulgada": 12, "pies": 1, "yardas": 0.333333, "milla": 0.000189394},
        "yardas": {"mm": 914.4, "cm": 91.44, "m": 0.9144, "km": 0.0009144,
                 "pulgada": 36, "pies": 3, "yardas": 1, "milla": 0.000568182},
        "milla": {"mm": 1609340, "cm": 160934, "m": 1609.34, "km": 1.60934,
                 "pulgada": 63360, "pies": 5280, "yardas": 1760, "milla": 1}
    }
    
    return distance * conversion_factors[from_unit][to_unit]

def convert_mass(mass, from_unit, to_unit):
    conversion_factors = {
        "mg": {"mg": 1, "g": 0.001, "kg": 0.000001, "t": 0.000000001, "ounce": 0.000035274, "pounds": 0.00000220462},
        "g": {"mg": 1000, "g": 1, "kg": 0.001, "t": 0.000001, "ounce": 0.035274, "pounds": 0.00220462},
        "kg": {"mg": 1000000, "g": 1000, "kg": 1, "t": 0.001, "ounce": 35.274, "pounds": 2.20462},
        "t": {"mg": 1000000000, "g": 1000000, "kg": 1000, "t": 1, "ounce": 35274, "pounds": 2204.62},
        "ounce": {"mg": 28349.5, "g": 28.3495, "kg": 0.0283495, "t": 0.0000283495, "ounce": 1, "pounds": 0.0625},
        "pounds": {"mg": 453592, "g": 453.592, "kg": 0.453592, "t": 0.000453592, "ounce": 16, "pounds": 1}
    }
    
    return mass * conversion_factors[from_unit][to_unit]

def convert_speed(speed, from_unit, to_unit):
    conversion_factors = {
        "m/s": {"m/s": 1, "km/h": 3.6, "yardas/s": 1.09361, "millas/h": 2.23694, "nudos": 1.94384},
        "km/h": {"m/s": 0.277778, "km/h": 1, "yardas/s": 0.09144, "millas/h": 0.621371, "nudos": 0.539957},
        "yardas/s": {"m/s": 0.9144, "km/h": 1.09728, "yardas/s": 1, "millas/h": 0.568182, "nudos": 0.493737},
        "millas/h": {"m/s": 0.44704, "km/h": 1.60934, "yardas/s": 1.76000, "millas/h": 1, "nudos": 0.868976},
        "nudos": {"m/s": 0.514444, "km/h": 1.852, "yardas/s": 1.09728, "millas/h": 1.15078, "nudos": 1}
    }
    
    return speed * conversion_factors[from_unit][to_unit]


def main():
    print_slow("Bienvenido al convertidor de la unidad!")
    
    while True:
        conversion_type = get_conversion_type()
        
        if conversion_type is None:
            print_slow("\nSalir del programa . . . ")
            time.sleep(0.02)
            break
        
        unit_from = get_measurement_unit(conversion_type)
        
        if unit_from is None:
            continue
        
        unit_to = get_measurement_unit(conversion_type)
        
        if unit_to is None:
            continue
        
        value = get_float_input(f"\nIngrese el valor en {unit_from}: ")
        
        if conversion_type == "1":
            if unit_from == "°C" and unit_to == "°F":
                converted_value = celsius_to_fahrenheit(value)
                print_slow(f"\n{value} {unit_from} es igual a {converted_value} {unit_to}.")
            elif unit_from == "°F" and unit_to == "°C":
                converted_value = fahrenheit_to_celsius(value)
                print_slow(f"\n{value} {unit_from} es igual a {converted_value} {unit_to}.")
        elif conversion_type == "2":
            converted_value = convert_distance(value, unit_from, unit_to)
            print_slow(f"\n{value} {unit_from} es igual a {converted_value} {unit_to}.")
        elif conversion_type == "3":
            converted_value = convert_mass(value, unit_from, unit_to)
            print_slow(f"\n{value} {unit_from} es igual a {converted_value} {unit_to}.")
        elif conversion_type == "4":
            converted_value = convert_speed(value, unit_from, unit_to)
            print_slow(f"\n{value} {unit_from} es igual a {converted_value} {unit_to}.")

if __name__ == "__main__":
    main()
    input('\n')