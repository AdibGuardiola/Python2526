

#1.1 Bucle con rango hasta 3

for i in range(3):
    print("Range:", i)

#1.2 Bucle que genera los primeros 40 numero ,empieza en 2 y va de 2 en 2

for i in range(2, 41, 2):
    print(i)

#1.3 grupo de amigos

amigos  = ["Pedro", "Pablo", "Juan"]

for par in amigos:
    print("Lista:", par)

#1.4 Bucle que va hasta 5 pero si encuentra el 2 se lo salta

for i in range(5):
    if i == 2:
        continue
    print("Continue:", i)


# 2 FOR CON DICCIONARIO (SOLO CLAVES),   sin .items() tengo que buscar el valor  con .items() ya lo tengo


amigos = {
    "Daniel": 20,
    "Lucia": 25,
    "Carlos": 18
}

for nombre in amigos:
    print(nombre, "tiene", amigos[nombre], "€")

for nombre, dinero in amigos.items():
    print(nombre, "tiene", dinero, "€")



# 3 FOR ANIDADO

matriz = [[1,2], [3,4]]

for fila in matriz:
    for numero in fila:
        print("Anidado:", numero)



# 4 Bucle dentro de bucle anidado


grupos = [
    ["Pedro", "Pablo"],
    ["Juan", "Luis"],
    ["Ana", "Lucia"]
]


for grupo in grupos:
    print("Grupo:")
    
    for amigo in grupo:
        print(" -", amigo)
