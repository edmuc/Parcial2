#1 Desarrollar un programa que determine si en una lista no existen elementos repetidos

entrada = input("Ingrese los elementos de la lista separados por comas: ")

lista = [x.strip() for x in entrada.split(",")]

if len(lista) == len(set(lista)):
    print("No existen elementos repetidos en la lista.")
else:
    print("Existen elementos repetidos en la lista.")




#2 Desarrollar un programa que determine si en una lista se encuentra una cadena de caractees con dos o mas volcales. Si la cadena existe debe imprimirla si no existe debe imprimir. No existe

lista1 = input("Ingrese los elementos de la lista separados por comas: ").split(',')

encontrada = False

for cadena in lista1:
    cadena = cadena.strip()
    contador_vocales = 0
   
    for letra in cadena.lower():
        if letra in "aeiou":
            contador_vocales += 1
    
    
    if contador_vocales >= 2:
        print("Cadena con dos o más vocales encontrada:", cadena)
        encontrada = True
          

if not encontrada:
    print("No existe")



#3 Desarrollar un programa que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda lista

lista1 = input("Ingrese los elementos de la lista 1 separados por comas: ").split(',')
lista2 = input("Ingrese los elementos de la lista 2 separados por comas: ").split(',')

lista1 = [x.strip() for x in lista1]
lista2 = [x.strip() for x in lista2]

resultado = set(lista1) - set(lista2)

print("Elementos que están en la primera lista y no en la segunda:", resultado)



#4 Desarrollar un algoritmo que calcule el promedio de un arreglo de reales

entrada = input("Ingrese los números separados por comas: ")
arreglo = [float(x) for x in entrada.split(",")]

suma = sum(arreglo)
promedio = suma / len(arreglo)

print("El promedio es:", promedio)

