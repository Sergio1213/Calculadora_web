# Función para realizar la suma de dos números
def suma(num1, num2):
    return num1 + num2

# Función para realizar la resta de dos números
def resta(num1, num2):
    return num1 - num2

# Función para realizar la multiplicación de dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Función para realizar la división de dos números
def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    return num1 / num2

# Función principal de la calculadora
def calculadora():
    print("Calculadora Simple")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        operacion = input("Seleccione la operación (1/2/3/4): ")
        
        if operacion not in ["1", "2", "3", "4"]:
            print("Opción no válida")
        else:
            if operacion == "1":
                resultado = suma(num1, num2)
            elif operacion == "2":
                resultado = resta(num1, num2)
            elif operacion == "3":
                resultado = multiplicacion(num1, num2)
            else:
                resultado = division(num1, num2)
            
            print("Resultado: ", resultado)
    except ValueError:
        print("Error: Ingrese números válidos")

if __name__ == "__main__":
    calculadora()
