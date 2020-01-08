class Node():
    def __init__(self, name):
        '''name is a string'''
        self.name = name
    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, source, dest):
        '''source and dest are nodes'''
        self.source = source
        self.dest = dest

    def getSrc(self):
        return self.source

    def getDest(self):
        return self.dest

    def __str__(self):
        return self.source.getName()+ "-->"+ self.dest.getName()

class Digraph():
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges={}

    def addNode(self,node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node]= []

    def addEdge(self, edge):
        src = edge.getSrc()
        dest = edge.getDest()
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
        
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self,name):
        for n in self.edges:
            if n.getName()== name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + "-->"+ dest.getName()+'\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDest, edge.getSrc)
        Digraph.addEdge(self,rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago','Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 

def dfs(graph, start, stop, path, shortest, toPrint = False):
    """Depth first search"""
    path= path + [start]
    if toPrint:
        print("Current DFS path: "+ printPath(path))
    if start == stop:
        return path
    for node in graph.childrenOf(start):
        if node not in path:# avoid cycles
            if shortest == None or len(path)< len(shortest):
                newPath = dfs(graph, node, stop, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print("Already visited "+ node.getName())
    return shortest

def shortestPath(graph, start, stop, toPrint=False):
    return dfs(graph, start, stop, [], None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    if sp != None:
        print('Shortest path from', source, 'to',destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

testSP('Boston', 'Phoenix') 


def bfs(graph, start, stop, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue)!=0:
        #Get and remove oldest element in path queue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print("Current BFS path:", printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode==stop:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)

    return None

def shortestPath(g, start, stop, toPrint=False):
    return bfs(g, start, stop, toPrint)

testSP('Boston', 'Phoenix') 
    