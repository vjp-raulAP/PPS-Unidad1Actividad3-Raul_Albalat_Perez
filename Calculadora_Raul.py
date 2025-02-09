#CALCULADORA COMPLETA
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    #Division de dos números, con control de división por cero.
    
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def mayorCero(a):
    #indica si el número pasado es mayor que cero.

    return a > 0

def is_number(valor):
    #indica si el argumento introducido es un número o no.

    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def pedir_numero(mensaje, validar_mayor_cero=False):
    #solicita un numero al usuario y valida la entrada.
    while True:
        valor = input(mensaje)

        if is_number(valor):
            num = float(valor)
            if validar_mayor_cero and not mayorCero(num):
                print("Error: El número debe ser mayor que cero.")
            else:
                return num
        else:
            print("Error: Debe ingresar un numero que sea valido.")

def calculadora():
    operaciones = {
        '1': ("Suma", suma),
        '2': ("Resta", resta),
        '3': ("Multiplicación", multiplicacion),
        '4': ("División", division),
        '5': ("Salir", None)
    }
    while True:
        print("\nSeleccione una operación:")
        for clave, (nombre, _) in operaciones.items():
            print(f"{clave}. {nombre}")

        operacion = input("ingrese el número de la operación (1/2/3/4/5): ")

        if operacion == '5':  #Opción para salir
            print("Saliendo de la calculadora... ")
            print(" Que tenga un buen día ")
            break

        if operacion in operaciones and operacion != '5':
            num1 = pedir_numero("ingrese el primer numero: ")

                # Si la operación es división, validar que num2 > 0
            if operacion == '4':
                num2 = pedir_numero("ingrese el segundo numero (debe ser mayor que 0): ", validar_mayor_cero=True)
            else:
                num2 = pedir_numero("ingrese el segundo numero: ")

            resultado = operaciones[operacion][1](num1, num2)
            print(f"Resultado: {resultado}")      
        else:
            print("operación no valida.")

if __name__=="__main__":
    calculadora()