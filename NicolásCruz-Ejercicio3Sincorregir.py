##EJERCICIO 3 SIN CORREGIR
nombre = input("Introduce nombre: ")
while nombre != nombre.ischar():
    print("Caracter incorrecto")
    nombre = input("Introduce nombre: ")
apellido = input("Introduce apellido: ")
while apellido != apellido.ischar():
    print("Caracter incorrecto")
    apellido = input("Introduce apellido: ")

alias = ("nombre[3].UPPER()","-","apellido[-3].UPPER()","-","len(nombre[3])-apellido[-3]")

print(alias)
