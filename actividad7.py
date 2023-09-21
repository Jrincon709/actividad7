from dataclasses import dataclass

@dataclass

class Elemento:
    nombre:str
    def __eq__(self, other: object):
        if isinstance( other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador:int = 0
    def __init__(self,nombre:str):
        self.listaelementos:list = []
        self.nombre:str = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador
    
    @property
    def _id(self):
        return self.__id
    
   
    
    def contiene (self, other:'Elemento')-> bool:
        for i in self.listaelementos:
            if other == i:
                return True
            else:
                return False
    
    def agregar_elemento (self,other:'Elemento'):
        if not self.contiene (other):
            self.listaelementos.append(other)
    
    def unir (self,conjunto:'Conjunto'):
        for i in conjunto.listaelementos:
            self.agregar_elemento(i)

    def add (self, other: 'Conjunto'):
        conjunto_resultante = Conjunto()
        conjunto_resultante.unir(other)
        return conjunto_resultante
    @classmethod

    def intersectar (cls, conjunto1:'Conjunto', conjunto2:'Conjunto'):
        elementos_comunes = [elemento for elemento in conjunto1.listaelementos if conjunto2.contiene(elemento)]
        nombre_conjunto = f"<{conjunto1.nombre}> <INTERSECTADO><{conjunto2.nombre}>"
        nuevoconjunto = Conjunto (nombre_conjunto)
        for i in elementos_comunes:
            nuevoconjunto.listaelementos.append(i)
            
    def  __str__ (self):
        elementoss= ",".join(  i.nombre for   i   in self.listaelementos )
        representacion= f"conjunto {self.nombre}:({elementoss})"
        return representacion
    
conjunto= Conjunto("sw")
minielementos=Elemento("elemento1")
elemento= Elemento("Elemento2")
elemento2= Elemento("Elemento3")

conjunto.agregar_elemento(minielementos)
conjunto.agregar_elemento(elemento)
conjunto.agregar_elemento(elemento2)


print(conjunto)
        

    

    