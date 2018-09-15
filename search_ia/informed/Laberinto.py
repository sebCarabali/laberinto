# -*- coding: utf-8 -*-
from math import sqrt

class SearchNode(object):
    """
        Representa un nodo de busqueda abstracto.
            estado: Representa el estado del nodo.
            padre : nodo que generó el nodo actual.
            accion: acción que generó el nodo actual.
            cost  : costo que tomó generar el nodo actual.
    """
    def __init__(self, estado, padre = None, accion = None, cost = 0):
        self.estado = estado
        self.padre = padre
        self.profundidad = 0
        self.accion = accion
        self.cost = cost
        if padre:
            self.profundidad = self.padre.profundidad + 1
            self.cost = padre.cost + 1
    
    def __eq__(self, value):
        return value.estado == self.estado

class SearchProblem(object):

    def __init__(self, estado_inicial):
        """
            Representa un problema de busqueda abstracto.
                estado_inicial: Estado inicial de busqueda.
        """
        self.estado_inicial = estado_inicial
    
    def es_objetivo(self, nodo):
        """
            Verifica si el nodo dado es un nodo objetivo.
                nodo: Nodo a probar.
        """
        raise NotImplementedError("es_objetivo")

    def sucesores(self, nodo):
        """
            Retorna los sucesores del nodo dado.
                nodo: Nodo a obtener los sucesores.
        """
        raise NotImplementedError("sucesores")

    def heuristic(self, nodo, nodo_objetivo):
        pass

    def euclidean(self, x1, x2, y1, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

class SearchAgent(object):
    """
        Representa un agente de busqueda.
    """

    def resolver(self, problema):
        """
            Resuelve un problema de busqueda.
                problema: Problema de busqueda a resolver extiende de la clase
                            SearchProblem.
        """
        raise NotImplementedError("resolver")



class NodoLaberinto(SearchNode):
    pass
    """
    def darxy(self):
        for i, l in enumerate(self.estado):
            for j,p in enumerate(l):
                if self.estado[i][j] == 2:
                    return (i, j)
        return None
    """
    def __repr__(self):
        return str(self.estado)

class Laberinto(SearchProblem):
    
    def __init__(self, estado_inicial, mapa):
        super(Laberinto, self).__init__(estado_inicial)
        self.mapa = mapa

    def es_objetivo(self, nodo):
        target = self.buscar_objetivo()
        return nodo.estado == target

    def buscar_objetivo(self):
        for i, l in enumerate(self.mapa):
            for j, k in enumerate(l):
                if self.mapa[i][j] == 3:
                    return (i, j)
        return None

    def sucesores(self, nodo):
        moves = [self.up, self.down, self.left, self.right]
        fns = [fn(nodo) for fn in moves]
        return [f for f in fns if f]
    
    def up(self, nodo):
        x = nodo.estado[0]
        y = nodo.estado[1]
        return NodoLaberinto((x-1, y), nodo, 'Up') if mapa[x-1][y] != 0 else None
    
    def down(self, nodo):
        x = nodo.estado[0]
        y = nodo.estado[1]
        return NodoLaberinto((x+1, y), nodo, 'Down') if mapa[x+1][y] != 0 else None
    
    def left(self, nodo):
        x = nodo.estado[0]
        y = nodo.estado[1]
        return NodoLaberinto((x, y-1), nodo, 'Left') if mapa[x][y-1] != 0 else None

    def right(self, nodo):
        x = nodo.estado[0]
        y = nodo.estado[1]
        return NodoLaberinto((x, y+1), nodo, 'Right') if mapa[x][y+1] != 0 else None

x, y = (1, 1)
n = NodoLaberinto((x, y))
mapa = [[0 ,0 ,0 ,0], [0, 2, 0, 0], [0, 1, 3, 0], [0, 0, 0, 0]]
l = Laberinto(n, mapa)
print(l.sucesores(n))
#o = NodoLaberinto((2,2))
#print(l.es_objetivo(n))
#print(l.es_objetivo(o))
#print(n.darxy())

