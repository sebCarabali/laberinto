# -*- coding: utf-8 -*-
from math import sqrt
import heapq


class SearchNode(object):
    """
        Representa un nodo de busqueda abstracto.
            estado: Representa el estado del nodo.
            padre : nodo que generó el nodo actual.
            accion: acción que generó el nodo actual.
            cost  : costo que tomó generar el nodo actual.
    """

    def __init__(self, estado, padre=None, accion=None, cost=0):
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

    def heuristica(self, nodo):
        return nodo.cost + self.euclidiana(nodo.estado, self.buscar_objetivo())

    def euclidiana(self, p, q):
        return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """

    def __init__(self):
        """
          heap: A binomial heap storing [priority,item]
          lists. 

          dict: Dictionary storing item -> [priorirty,item]
          maps so we can reach into heap for a given 
          item and update the priorirty and heapify
        """
        self.heap = []
        self.dict = {}

    def setPriority(self, item, priority):
        """
            Sets the priority of the 'item' to
        priority. If the 'item' is already
        in the queue, then its key is changed
        to the new priority, regardless if it
        is higher or lower than the current 
        priority.
        """
        if item in self.dict:
            self.dict[item][0] = priority
            heapq.heapify(self.heap)
        else:
            pair = [priority, item]
            heapq.heappush(self.heap, pair)
            self.dict[item] = pair

    def getPriority(self, item):
        """
            Get priority of 'item'. If 
        'item' is not in the queue returns None
        """
        if not item in self.dict:
            return None
        return self.dict[item][0]

    def dequeue(self):
        """
          Returns lowest-priority item in priority queue, or
          None if the queue is empty
        """
        if self.isEmpty():
            return None
        (priority, item) = heapq.heappop(self.heap)
        del self.dict[item]
        return item

    def isEmpty(self):
        """
            Returns True if the queue is empty
        """
        return len(self.heap) == 0


class AStar(SearchAgent):

    def resolver(self, problema):
        abiertos = PriorityQueue()
        cerrados = []
        abiertos.setPriority(problema.estado_inicial,
                             problema.heuristica(problema.estado_inicial))
        while not abiertos.isEmpty():
            actual = abiertos.dequeue()
            if problema.es_objetivo(actual):
                movimientos = []
                while actual:
                    movimientos.append(actual)
                    actual = actual.padre
                movimientos.reverse()
                return movimientos
            cerrados.append(actual)
            hijos = problema.sucesores(actual)
            for h in hijos:
                fn = problema.heuristica(h)
                if h not in cerrados or not abiertos.getPriority(h):
                    abiertos.setPriority(h, fn)
                #else:
                #    if abiertos.getPriority(h) > fn:
                #        abiertos.setPriority(h, fn)
                        
        return "No solucion"


x, y = (1, 1)
n = NodoLaberinto((x, y))

mapa = [
    [0, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 1, 3, 0],
    [0, 0, 0, 0]
]
mapa.sort()
l = Laberinto(n, mapa)
a = AStar()
s = a.resolver(l)
print(s)
#o = NodoLaberinto((2,2))
# print(l.es_objetivo(n))
# print(l.es_objetivo(o))
# print(n.darxy())
