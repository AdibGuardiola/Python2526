# 4 Funciones

# 1 Funcion básica

def saludar():
    print("Hola, bienvenido!")

saludar()

# 2 Funciones con parámetros

def saludar_personas(nombre):
    print("Hola", nombre, "bienvenido!")

saludar_personas("Juan")

# 2.1 Función con varios parámetros 

def mostrar_edad(nombre, edad):
    print("Hola", nombre, "tienes", edad, "años")

mostrar_edad("Pepe", 35)



# 3 Funciones utilizando return 

# 3.1 Función sin utilizar return

def sumar(a, b):
    print(a + b)

resultado = sumar(5, 6)

print (resultado)

# 3.2 Función con return

def sumar(a, b):
    return a + b

print(sumar(5, 6))

# 3.3 Funcion introduciendo parámetros

def sumar(a, b):
    return a + b

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))

print("La suma de los números es:", sumar(num1, num2))

#3.3 Función introducioendo parámetros ,caso especial 

def mostrar_edad():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    
    print("Hola " + nombre + ", tienes " + str(edad) + " años")
#Otra manera
    print("Hola", nombre, ", tienes", edad, "años")
#Otra manera_2
    print(f"Hola {nombre}, tienes {edad} años")

mostrar_edad()


# 4 Funciones con condicional

def mayordeedad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "No es mayor de edad"

resultado = int(input("dime tu edad: "))

print(mayordeedad(resultado))

# 5 Funcion con listas

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
alturas = [1.75, 1.80, 1.70, 1.85, 1.90]

print("La suma de la lista es:", sumar_lista(alturas))

# 6 Funciones condicional con listas   

def filtar_mayores(lista):
    mayores = []
    
    for numero in lista:
        if numero > 5:
            mayores.append(numero)
    return mayores

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Los números mayores a 5 son:", filtar_mayores(numeros))

#7 Concepto de tupla 
datos = (10, 20)

# Acceder a valores
print(datos[0])
print(datos[1])

# Función que devuelve una tupla
def ejemplo():
    return 5, 10

a, b = ejemplo()
print(a, b)

# Usar tuplas en un bucle
personas = [("Juan", 20), ("Ana", 17)]

for nombre, edad in personas:
    print(nombre, edad)

#8 Funciones aplicando análisis de listas

def analizar_notas(notas):
    
    aprobados = 0
    suspensos = 0
    
    for nota in notas:
        if nota >= 5:
            aprobados += 1
        else:
            suspensos += 1
    return aprobados, suspensos

notas = [5, 6, 7, 8, 9, 10, 4, 3, 2, 1]

aprobados, suspensos = analizar_notas(notas)

print("Aprobados:", aprobados)
print("Suspensos:", suspensos)

#9 Funcion busqueda de parámetros en lista

def buscarnumero(lista, objeto):
    contador = 0
    
    for numero in lista:
        if numero == objeto:
            contador += 1
            
    return contador

print(buscarnumero([1,3,2,2,2,4,3], 2))
