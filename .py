import re

def calculadora():
    print("Bienvenido a la calculadora. Por favor, ingresa la operación (ejemplo: 15+24 o 42*3).")
    entrada = input("Ingrese su operación: ")
    
    # Utilizar expresiones regulares para encontrar números y operadores
    partes = re.findall(r"([-+]?\d*\.?\d+|[*/+-])", entrada.replace(" ", ""))
    
    # Verificar si se encontraron exactamente tres partes: número1, operador, número2
    if len(partes) != 3:
        return "Error: Formato de entrada no válido. Asegúrate de ingresar algo como '15+24' o '42*3'."
    
    num1, operador, num2 = partes
    num1 = float(num1)
    num2 = float(num2)

    # Realiza la operación basada en el operador ingresado
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            return "Error: División por cero no permitida."
        resultado = num1 / num2
    else:
        return "Error: Operador no válido. Usa +, -, * o /."
    
    return f"El resultado es {resultado}"
print(calculadora())
