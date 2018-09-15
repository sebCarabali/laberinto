# -*- coding: utf-8 -*-

from searchagent import SearchAgent
from searchproblem import SearchProblem

class DfsIterative(SearchAgent):

    def __init__(self, limite):
        self.limite = limite

    def resolver(self, problema):
        profundidad = 0
        actual = problema.estado_inicial
        while profundidad < self.limite:
            res = self.bpl(actual, problema, profundidad)
            if res:
                sol = []
                while res:
                    sol.append(res)
                    res = res.padre
                sol.reverse()
                return sol
            profundidad += 1
        return "No encontrado."
    
    def bpl(self, nodo, problema, profundidad):
        if profundidad == 0 and problema.es_objetivo(nodo):
            return nodo
        elif profundidad > 0:
            for h in problema.sucesores(nodo):
                res = self.bpl(h, problema, profundidad-1)
                if res:
                    return res
        else:
            return None
