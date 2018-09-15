# -*- coding: utf-8 -*-

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
        if padre:
            self.profundidad = self.padre.profundidad + 1
    
    def __eq__(self, value):
        return value.estado == self.estado
        
    