import os
from Menus import Menu
from listas import Lista
from cola import Cola
from pila import Pila


opc =""
while opc !="4":
    os.system("cls")
    men = Menu("Menu Estructuras",["1) Listas","2) Colas","3) Pilas","4) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        lista1 = Lista()
        while opc1 !="7":
            os.system("cls")
            men1 = Menu("\033[3;36m"+"Menu Listas",["\033[0;33m"+"1) Añadir","2) Obtener","3) Mostrar","4) Buscar","5) Insertar","6) Eliminar","7) Salir"])
            opc1 = men1.menu()
            os.system("cls")

            if opc1 == "1":
                print("Ingresar elementos a la Lista")
                dato = input("Ingrese un dato a la Lista: ")
                lista1.append(dato)
                print(lista1.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "2":
                print("Obtener Elemento")

            elif opc1 == "3":
                print("Mostrar elementos")
                #lista1 = Lista()
                lista1.mostrar()
                input("Presione una tecla para continuar...")

            elif opc1 == "4":
                print("Buscar un dato en la lista y retornar su posicion")
                dato = input("Ingrese el dato a buscar en la Lista: ")
                print(lista1.buscar(dato))
                # print(lista1.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "5":
                print("Insertar un dato en la lista")
                dato = input("Ingrese el dato a insertar en la Lista: ")
                lista1.insertar(dato)
                print(lista1.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "6":
                print("Eliminar un dato de la lista")
                dato = input("Ingrese esl dato a eliminar de la Lista: ")
                lista1.eliminar(dato)
                print(lista1.lista)
                input("Presione una tecla para continuar...")

    elif opc == "2":
        opc2 =""
        cola1 = Cola()
        while opc2 !="4":
            os.system("cls")
            men2 = Menu("\033[3;36m"+"Menu Colas",["\033[0;33m"+"1) Encolar","2) Desencolar","3) Mostar","4) Salir"])
            opc2 = men2.menu()
            os.system("cls")

            if opc2 == "1":
                print("Encolar elementos")
                dato = input("Ingrese el dato a encolar: ")
                cola1.encolar(dato)
                print(cola1.cola)
                input("Presione una tecla para continuar...")

            elif opc2 == "2":
                print("Desencolar elemento de la cola")
                cola1.desencolar()
                print(cola1.cola)
                input("Presione una tecla para continuar...")

            elif opc2 == "3":
                print("Mostrar elementos")
                #lista1 = Lista()
                cola1.mostrar()
                print(cola1.cola)
                input("Presione una tecla para continuar...")

    elif opc =="3":
        opc3 =""
        pila1 = Pila()
        while opc3 !="5":
            os.system("cls")
            men3 = Menu("\033[3;36m"+"Menu Pilas",["\033[0;33m"+"1) Ingresar","2) Eliminar.","3) Mostrar","4) Longitud","5) Salir"])
            opc3 = men3.menu()
            os.system("cls")

            if opc3 == "1":
                print("Ingresar elementos a la Pila")
                dato = input("Ingrese un dato a la Pila: ")
                pila1.push(dato)
                print(pila1.lista)
                input("Presione una tecla para continuar...")

            elif opc3 == "2":
                print("Eliminar un elemento de la Pila")
                dato = pila1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La lista esta vacia")
                input("Presione una tecla para continuar...")

            elif opc3 == "3":
                print("Mostrar los elementos de la pila")
                pila1.show()
                print(pila1.lista)
                input("Presione una tecla para continuar...")

            elif opc3 == "4":
                print("Mostar longitud de la Pila")
                pila1.longitud()
                print(pila1.lista)
                input("Presione una tecla para continuar...")


    elif opc == "4":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")