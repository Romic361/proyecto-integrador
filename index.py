lista =[]
n = 0
v = 0

print()
while n == 0:
     list.clear(lista)
     while n < 5:
          lista.append(int(input("Valor a calcular: ")))  
          n += 1
          v += 1
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

     while n > 0:
               if vMenu== 1:
                    print(f"La suma total es: {suma(lista)}")
                    v =int(input("Seguir usando los mismos valores? [1=si, 2=no]: "))
                    if v == 1:
                         vMenu = int(input("Elegir operación a realizar: "))
                    else: 
                         n=0
               else:
                    if vMenu== 2:
                         print(f"El promedio es: {suma(lista)/5}")
                         v =int(input("Seguir usando los mismos valores? [1=si, 2=no]: "))
                         if v == 1:
                              vMenu = int(input("Elegir operación a realizar: "))
                         else: 
                              n=0
                    else:
                         if vMenu== 3:
                              print((f"El mayor numero es: {max(lista)}"))
                              v =int(input("Seguir usando los mismos valores? [1=si, 2=no]: "))
                              if v == 1:
                                   vMenu = int(input("Elegir operación a realizar: "))
                              else: 
                                   n=0
                         else: 
                              if vMenu== 4:
                                   print((f"El menor numero es: {min(lista)}"))
                                   v =int(input("Seguir usando los mismos valores? [1=si, 2=no]: "))
                                   if v == 1:
                                        vMenu = int(input("Elegir operación a realizar: "))
                                   else: 
                                        n=0
                              else: 
                                   print("Valor ingresado no corresponde a una opción del menú.")
                                   vMenu = int(input("Elegir operación a realizar: "))
                                 


print()
