from bfs import Bfs
from searchnode import SearchNode
from searchproblem import SearchProblem
from dfs import Dfs
from dfsl import DfsLimited
from dfsi import DfsIterative

class LinNode(SearchNode):
    
    def __repr__(self):
        return "({}, {})".format(self.estado, self.accion)
    
class LinProblem(SearchProblem):

    def es_objetivo(self, nodo):
        return nodo.estado == [1, 2, 3, 4]
    
    def sucesores(self, nodo):
        fns = [self.D, self.C, self.I]
        x = [fn(nodo) for fn in fns]
        return [y for y in x if y]
    
    def D(self, nodo):
        cpy = nodo.estado[:]
        cpy[0], cpy[1] = cpy[1], cpy[0]
        return LinNode(cpy, padre = nodo, accion= 'D')
    
    def C(self, nodo):
        cpy = nodo.estado[:]
        cpy[1], cpy[2] = cpy[2], cpy[1]
        return LinNode(cpy, padre = nodo, accion= 'C')
    
    def I(self, nodo):
        cpy = nodo.estado[:]
        cpy[2], cpy[3] = cpy[3], cpy[2]
        return LinNode(cpy, padre = nodo, accion= 'I')


lnode = LinNode([4, 3, 2, 1])
lprom = LinProblem(lnode)
"""
bfs = Bfs()
s = bfs.resolver(lprom)


dfs = Dfs()
s = dfs.resolver(lprom)


dfsl = DfsLimited(3)
s = dfsl.resolver(lprom)
"""
dfsi = DfsIterative(7)
s = dfsi.resolver(lprom)
print(s)