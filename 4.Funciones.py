# ==========================================
# 1. FUNCIÓN BÁSICA (sin bucles ni condicionales)
# ==========================================

def saludar():
    print("Hola, bienvenido al programa")

saludar()


# ==========================================
# 2. FUNCIÓN CON PARÁMETRO
# ==========================================

#Parámetro =>nombre
#Argumento =>Adib

def saludar_persona(nombre):
    print("Hola "+ nombre)
    

saludar_persona("10")

#2.1 FUNCIÓN CON PARÁMETRO ,incluimos un strime

def mostrar_edad(nombre, edad):
    print("Hola " + nombre + ", tienes " + str(edad) + " años")

mostrar_edad("Adib", 25)


# ==========================================
# 3. FUNCIÓN CON RETURN
# ==========================================

#3.1 De forma inicial no funciona
def sumar(a, b):
    print(a + b)

resultado = sumar(5, 3)
print(resultado)


#3.2 Ahora si

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)

#3.3 Incluimos un input
def sumar(a, b):
    return a + b


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

resultado = sumar(num1, num2)

print("La suma es:", resultado)

# ==========================================
# 4. FUNCIÓN CON CONDICIONAL
# ==========================================

def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

# pedir dato al usuario
edad = int(input("Introduce tu edad: "))

# usar la función
resultado = es_mayor_de_edad(edad)

# mostrar resultado
print(resultado)


# ==========================================
# 7. FUNCIÓN QUE TRABAJA CON LISTAS
# ==========================================

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]
print("Suma total:", sumar_lista(numeros))


# ==========================================
# 8. FUNCIÓN QUE FILTRA DATOS (condicional + lista)
# ==========================================

def filtrar_mayores(lista):
    mayores = []
    
    for numero in lista:
        if numero > 5:
            mayores.append(numero)
    
    return mayores

print(filtrar_mayores([2, 7, 1, 9, 4]))


# ==========================================
# 9. FUNCIÓN MÁS COMPLETA (simulación real)
# ==========================================

def analizar_notas(notas):
    
    aprobados = 0
    suspensos = 0
    
    for nota in notas:
        if nota >= 5:
            aprobados += 1
        else:
            suspensos += 1
    
    return aprobados, suspensos

resultado = analizar_notas([4, 6, 7, 3, 9])
print("Aprobados:", resultado[0])
print("Suspensos:", resultado[1])


# ==========================================
# 10. FUNCIÓN CON TODO (parámetros + bucle + condicional + return)
# ==========================================

def buscar_numero(lista, objetivo):
    
    for numero in lista:
        if numero == objetivo:
            return "Encontrado"
    
    return "No encontrado"

print(buscar_numero([1, 3, 5, 7], 5))
print(buscar_numero([1, 3, 5, 7], 2))