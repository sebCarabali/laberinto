# -*- coding: utf-8 -*-

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