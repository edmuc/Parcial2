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
