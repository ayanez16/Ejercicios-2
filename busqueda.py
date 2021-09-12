class Lista:
    def __init__(self,listas):
        self.__lista = listas

    @property
    def lista(self):        # getproperty
            return self.__lista

    # @lista.setter
    # def lista(self,value):  # setproperty
    #     self.__lista=value

    # busca un valor en la lista; retorna la posicion si lo encuentra
    #y si no lo encuentra retorna -1
    def busquedaLineal(self,buscado):
        pos=0
        enc=False
        lon = len(self.__lista)
        #recorre la lista hasta que la posicion sea igual a la longitud o enc sea verdadero
        while pos < lon and enc==False:
            if self.__lista[pos]["Nombre"] == buscado:
                enc=True
            else:
                pos = pos +1
        if enc : return pos
        else: return -1

    # def ordenar(self):
    #     for pos in range(0,len(self.__lista)):
    #         for sig in range(pos+1,len(self.__lista)):
    #             if self.__lista[pos]["Nombre"] > self.__lista[sig]["Nombre"]:
    #                 aux = self.__lista[pos]
    #                 self.__lista[pos]=self.__lista[sig]
    #                 self.__lista[sig]=aux

    def ordenarQuicksort(self):
        pass

    def ordenar(self,orden):
        orden = orden.lower()
        if orden == "asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["Nombre"] > self.__lista[sig]["Nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
        else:
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["Nombre"] < self.__lista[sig]["Nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux

    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin = len(self.lista)-1
        inicio = 0
        enc = False
        while inicio <= fin and enc ==False:
            medio = (inicio+fin)//2
            if self.lista[medio]["Nombre"] == buscado: enc= True
            elif self.lista[medio]["Nombre"] < buscado: inicio = medio+1
            else: fin = medio-1
        if enc: return medio
        else: return -1

notas = [
    {"Nombre":"Angel","n1":20,"n2":40},
    {"Nombre":"Danny","n1":30,"n2":50},
    {"Nombre":"Dayana","n1":40,"n2":50},
    {"Nombre":"Erick","n1":50,"n2":40},
    {"Nombre":"Romina","n1":55,"n2":40},
    {"Nombre":"Yadi","n1":60,"n2":40}
]

bus = Lista(notas)
# posicion = bus.busquedaLineal("Erick")
# if posicion != -1:
#     print(bus.lista[posicion])
# else:
#     print("Nombre no se encuentra en la lista")
# bus.ordenar()
# bus.ordenar("des")
# print(bus.lista)
# print(bus.busquedaLineal("Danny"))
# bus = Lista([2,4,6])
# bus.lista = [3,5]
# print(bus.lista)
posicion = bus.busquedaBinaria("Yadi")
if posicion != -1:
    print(bus.lista[posicion])
else:
    print("Nombre no se encuentra en la lista")