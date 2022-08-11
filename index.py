lista =[]
n = 0

print()

while n < 5:
     lista.append(int(input("Valor a calcular: ")))
     n += 1
print()
print("\t MENU: ")
print("1- Suma")
print("2- Promedio")
print("3- Máximo valor")
print("4- Mínimo valor ")
print()
vMenu = int(input("Elegir operación a realizar: "))
print()

def suma(lista):
     for elemento in lista:
          suma_total = sum(lista)
          return suma_total



if vMenu== 1:
     print(f"La suma total es: {suma(lista)}")


else:
     print("Valor ingresado no corresponde a una opción del menú.")

print()
 
