# -*- coding: utf-8 -*-

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

    def heuristic(self, nodo):
        pass
