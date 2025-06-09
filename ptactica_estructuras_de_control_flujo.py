#Desarrolle un programa que calcule la suma de los enteros del 1 al 100, es decir: 1 + 2 + 3 + … + 99 + 100
"""suma=0
for i in range (0,101):
    suma +=i
    i+=1
print(suma) """
#Escriba un programa que reciba un entero positivo. 
# Sí el número ingresado es múltiplo de 5 deberá imprimir en pantalla El número es múltiplo de 5, en cualquier otro caso deberá imprimir 
# El número no es múltiplo de 5.
"""numero= int(input("ingrese un numero"))
if numero %5 == 0:
    print(numero,"es multiplo de 5")
else:
    print(numero, "no es multipplo de 5")"""
#Escriba un programa que reciba como entrada una frase (un string) y determine cuántas veces aparece cada una de las vocales en esa frase. 
# El valor de salida a mostrar debe ser un diccionario
"""frase =input("ingrese una frase")
vocales={"a":0,"e":0,"i":0,"o":0,"u":0}
for letra in frase :
    if letra in vocales:
        vocales [letra]+=1
print (vocales.items())"""
#Escribe un programa que pida cinco números y cuente cuántos de ellos son mayores que 10
# Inicializar el contador
"""contador = 0

# Usar un bucle for para pedir 5 números
for i in range(5):
    numero = float(input(f"Introduce el número {i + 1}: "))
    if numero > 10:
        contador += 1

# Mostrar cuántos números fueron mayores que 10
print(f"Has introducido {contador} números mayores que 10.")"""
#Escribe un programa que pida tres números y determine cuál es el mayor.
"""numero1= int(input("ingrese unel primer numero: "))
numero2= int(input("ingrese el segundo numero: "))
numero3= int(input("ingrese el tercer numero: "))
if numero1 > numero2 and numero1 >numero3:
        print ("el mayo es ", numero1)
elif numero2 >numero1 and numero2 >numero3:
        print ("el mayor es ", numero2)
else:
        print ("el mayor es el ", numero3 )
        """


#Escribe un programa que pida dos números y cuente cuántos múltiplos de 3 hay entre ellos.
"""nro1=int(input("ingrese un numero: "))
nro2=int(input("ingrese otro numero: " ))
#aseguramos que el numero menos vaya en primer orden.
if nro1 > nro2 :
        nro1,nro2= nro2, nro1
contador =0       
for numero in range(nro1,nro2+1):
        if numero % 3 ==0:
                contador +=1

print("La cantidad de numeros multiples de 3 entre",nro1," y ", nro2," es de:", contador )"""
#Escribe un programa que imprima los números del 1 al 10 en orden inverso.
"""for i in range(10,0,-1):
        print (i)"""
#Escribe un programa que muestre un menú con tres opciones: sumar dos números, restar dos números o multiplicar dos números. El programa debe repetirse hasta que el usuario elija salir.
"""
opcion= 0
while opcion != 4:
        print ("opcion 1 suma dos numeros")
        print ("opcion 2 resta dos numeros")
        print ("opcion 3 multiplica dos numeros")
        print ("opcion 4 salirs")

        opcion= int(input("ingrese una opcion"))
        if opcion == 1:
                n1=int(input("ingrese el n1"))
                n2=int(input("ingrese el n2"))
                print("la suma entre ",n1, "y ", n2, "es:", n1+n2)
        elif  opcion ==2:
                n1=int(input("ingrese el n1"))
                n2=int(input("ingrese el n2"))
                print("la resta entre ",n1, "y ", n2, "es:", n1-n2)
        elif opcion == 3:
                n1=int(input("ingrese el n1"))
                n2=int(input("ingrese el n2"))
                print("la multiplicacion entre ",n1, "y ", n2, "es:", n1*n2)
        elif opcion == 4:
                print("saliendo del programa.")
        else:
                 print("el nro ingresado no corresponde a las opciones, intente n uevamente")"""

#Escribe un programa que permita al usuario adivinar un número secreto entre 1 y 10, con un máximo de 5 intentos. Si el usuario acierta el número, el programa debe finalizar con un mensaje de felicitación. Es obligatorio el uso de la instrucción break. 
# Definir el número secreto
numero_secreto = 7

# Inicializar el número de intentos
intentos = 0

# Usar un bucle para permitir hasta 5 intentos
while intentos < 5:
    numero = int(input("Adivina el número (entre 1 y 10): "))
    
    if numero == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break  # Salir del bucle si el número es correcto
    else:
        print("Número incorrecto. Inténtalo de nuevo.")
    
    intentos += 1

if intentos == 5 and numero != numero_secreto:
    print("Lo siento, has agotado todos los intentos.")