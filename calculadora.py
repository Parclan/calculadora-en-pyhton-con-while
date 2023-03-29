

#Limpiar terminal
import os
os.system ('cls')
    
        
# valores para digitar el numero
num1 = int(input('Ingrese el numero 1:  '))
num2 = int(input('Ingrese el numero 2: '))

eleccion = 0 # variable para hacer la eleccion

# este sera un ciclo repetitivo para elegir una opcion
while eleccion != 6:
    print("""
    Ingrese la opcion:
          
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Cambio de valores
    6) Salir""")
    
    eleccion = int(input()) #renombramos la varible para otorgar una eleccion
    
    if eleccion == 1: 
        print(" ")
        print(F"Resultado: {num1} + {num2} = {num1 + num2}")
    
    elif eleccion == 2:
        print(" ")
        print(F"Resultado: {num1} - {num2} = {num1 - num2}")
    
    elif eleccion == 3:
        print(" ")
        print(F"Resultado: {num1} x {num2} = {num1 * num2}")
    
    elif eleccion == 4:
        print(" ")
        print(F"Resultado: {num1} ÷ {num2} = {num1 / num2}")
        
    elif eleccion == 5:
        num1 = int(input('Ingrese el numero 1: '))
        num2 = int(input('Ingrese el numero 2: '))
        
    elif eleccion == 6:
        print(F"Finalizado")
        break