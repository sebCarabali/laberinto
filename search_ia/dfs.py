# -*- coding: utf-8 -*-

from searchagent import SearchAgent
from searchproblem import SearchProblem

class Dfs(SearchAgent):

    def resolver(self, problema):
        abiertos = [problema.estado_inicial]
        cerrados = []
        while len(abiertos) > 0:
            actual = abiertos.pop()
            cerrados.append(actual)

            if problema.es_objetivo(actual):
                sol = []
                while actual:
                    sol.append(actual)
                    actual = actual.padre
                sol.reverse()
                return sol
            
            hijos = problema.sucesores(actual)
            for h in hijos:
                if h not in abiertos and h not in cerrados:
                    abiertos.append(h)
            
        return "Solucion no encontrada"

