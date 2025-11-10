1 #Desarrollar un programa que determine si en una lista no existen elementos repetidos

entrada = input("Ingrese los elementos de la lista separados por comas: ")

lista = [x.strip() for x in entrada.split(",")]

if len(lista) == len(set(lista)):
    print("No existen elementos repetidos en la lista.")
else:
    print("Existen elementos repetidos en la lista.")
