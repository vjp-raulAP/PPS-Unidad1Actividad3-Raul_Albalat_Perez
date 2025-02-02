
# CALCULADORA COMPLETA
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if not mayorCero(b):
        print ("El divisor debe de ser mayor que cero")
        return False
    else: 
        resultado = a / b
        return resultado

def is_Number(value):
    """Devuelve True si el valor es un número, False en caso contrario."""
    if value is None:
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False

def mayorCero(value):
    """Devuelve True si número es mayor que cero, False en caso contrario."""
    return value > 0

def main():
    
    """Programa principal para interactuar con el usuario."""
    print("Esto es Mi calculadora.")
    
    # Solicitar los dos números al usuario
    num1 = input("Introduce el primer número: ")
    while not is_Number(num1):
        num1 = input("Lo siento esto no es un número. Introduce un número válido: ")
    num1 = float(num1)

    num2 = input("Introduce el segundo número: ")
    while not is_Number(num2):
        num2 = input("Lo siento no es un número. Introduce un número válido: ")
    num2 = float(num2)

    #  menú de operaciones
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir de la la calculadora")
        
        opcion = input("Introduce el número: ")
        
        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

# Llamada al programa principal
if __name__ == "__main__":
    main()