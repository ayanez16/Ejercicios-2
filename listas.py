class Lista:
    def __init__(self,tamaño=3):
        self.lista = []
        self.longitud = 0
        self.size = tamaño

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
        else:
            print("La lista esta llena")

    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None #no retorna ningun valor
        else:
            return self.lista[pos]

    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range (pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]]
            self.longitud -=1
            self.lista = listaAux
            return [self.lista,eliminado]

#busca un dato en la lista y retorna la posicion de ese valor en la lista
    def buscar(self,dato):
        for pos,ele in enumerate(self.lista):
            if ele == dato:
                enc=True
                break
        if enc ==True:
            return pos
        else:
            return -1

#busca un dato con el metodo buscar y si no o encuentra lo inserta
    def insertar(self,dato):
        if self.buscar(dato):
            self.append(dato)
        else:
            print("El dato ya se encuentra en la lista")

#busca el dato a eliminar con el metodo buscar y si lo encuentra lo elimina de la lista
    def eliminar(self,dato,pos):
        self.buscar(dato)
        self.obtenerEliminado(pos)

    def mostrar(self):
        print("{:3}{:9} {}".format("","lista","Posicion")) #{:3} etc poner espacios
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:3}".format(ele,pos))


lista1 = Lista()
lista1.append("Damaris")
lista1.append(19)
lista1.append(True)
# lista1.mostrar()
# posicion = int(input("Ingrese posicion para obtener el elemento: "))
# resp = lista1.obtener(posicion)
# if resp == None:
#     print("Posicion no valida, verifique la lista...!!!")
# else:
#     print("El elemento de la posicion: {} es: {}".format(posicion,resp))

# posicion = int(input("Ingrese posicion del elemento a eliminar: "))
# resp = lista1.obtenerEliminado(posicion)
# if resp == None:
#     print("Posicion no valida, verifique la lista...!!!")
# else:
#     print("El elemento de la posicion: {} es: {}".format(posicion,resp))

# print(lista1.buscar("Damaris"))
# dato=3
# resp = lista1.buscar(dato)
# if resp !=-1:
#     print("Numero = {}se encuentra en la Posicion:({})de la lista:{}".format(dato,resp, lista1.lista))
# else:
#     print("Numero = {} no se encuentra en la lista:{}".format(dato,lista1.lista))
lista1.insertar(3)