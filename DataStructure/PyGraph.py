# 定义图的结点
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)+' connected to: '+ str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# 广度优先遍历
from collections import deque

def breadth_first_search(graph,root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root
    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
    return visited_vertices

def depth_first_search(graph,root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root
    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
                continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
    return visited_vertices


if __name__ == '__main__':
    # g = Graph()
    # for i in range(6):
    #     g.addVertex(i)
    # g.addEdge(0,1,5)
    # g.addEdge(0,5,2)
    # g.addEdge(1,2,4)
    # g.addEdge(2,3,9)
    # g.addEdge(3,4,7)
    # g.addEdge(3,5,3)
    # g.addEdge(4,0,1)
    # g.addEdge(5,4,8)
    # g.addEdge(5,2,1)
    # for v in g:
    #     for w in v.getConnections():
    #         print("( %s , %s )"%(v.getId(),w.getId()))
    g = dict()
    g['A'] = ['B','G','D']
    g['B'] = ['A','F','E']
    g['C'] = ['F','H']
    g['D'] = ['F','A']
    g['E'] = ['B','G']
    g['F'] = ['B','D','C']
    g['G'] = ['A','E']
    g['H'] = ['C']
    print(breadth_first_search(g,'B'))
    g2 = dict()
    g2['A'] = ['B','S']
    g2['B'] = ['A']
    g2['S'] = ['A','G','C']
    g2['D'] = ['C']
    g2['G'] = ['S','F','H']
    g2['H'] = ['G']
    g2['E'] = ['C']
    g2['F'] = ['G']
    g2['C'] = ['D','S','E']
    print(depth_first_search(g2,'B'))

