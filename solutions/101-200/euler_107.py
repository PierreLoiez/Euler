import pathlib
import time
from math import *

class Edge(object):
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
    def __str__(self):
        return f'{self.cost}, {self.start}, {self.end}'
    
    def __gt__(self, v1):
        return self.cost>v1.cost
    def __lt__(self, v1):
        return self.cost<v1.cost
    def __ge__(self, v1):
        return self.cost>=v1.cost
    def __le__(self, v1):
        return self.cost<=v1.cost
    

class Graph(object):
    def __init__(self, matrix):
        self.vertices = list(range(len(matrix)))
        self.edges = []
        createdLinks = []
        self.organizedEdges = {i:[] for i in self.vertices}
        self.accessible = {i:set() for i in self.vertices}
        for l in range(len(matrix)):
            for c in range(len(matrix)):
                if matrix[l][c] != -1 and (max(l, c), min(l, c)) not in createdLinks:
                    createdLinks.append((max(l, c), min(l, c)))
                    self.edges.append(Edge(l, c, matrix[l][c]))
                    self.accessible[l].add(c)
                    self.accessible[c].add(l)
                    self.organizedEdges[l].append(self.edges[-1])
                    self.organizedEdges[c].append(self.edges[-1])
        self.edges.sort()
        seenNodes = set()
        for i in range(40):
            seenNodes.add(self.edges[i].start)
            seenNodes.add(self.edges[i].end)
        print(seenNodes)
    def getValid(self):
        for vertex1 in self.vertices:
            for vertex2 in self.vertices:
                if not self.isPathToFrom(vertex1, vertex2):
                    return False
        return True
    def getEdgesOf(self, vertex):
        return self.organizedEdges[vertex]
    def refreshAccessible(self):
        self.accessible = {i:set() for i in self.vertices}
        self.organizedVertices = {i:[] for i in self.vertices}
        for edge in self.edges:
            self.accessible[edge.start].add(edge.end)
            self.accessible[edge.end].add(edge.start)
            self.organizedVertices[edge.start].append(edge)
            self.organizedVertices[edge.end].append(edge)

    def getNetValue(self):
        return sum(v.cost for v in self.edges)
        
    def isPathToFrom(self, start, end, seen=None):
        if start == end:
            return True
        if end in self.accessible[start]:
            return True
        if seen is None:
            seen = []
        for vertex in self.accessible[start]:
            if vertex in seen:
                continue
            seen.append(vertex)
            if self.isPathToFrom(vertex, end, seen):
                return True
        return False
    
def minCostV(dictionary, possible=None):
    if possible == None:
        possible = list(dictionary.keys())
    else:
        possible = possible[:]
    toRet = possible[0]
    smallest = 10**10
    for p in possible:
        if dictionary[p] < smallest:
            toRet = p
            smallest = dictionary[p]
    return toRet

def Prim(graph:Graph):
    # Using Prim's Algorithm
    cheapestCost, cheapestEdge = {v:10**10 for v in graph.vertices}, {v:None for v in graph.vertices}
    explored = []
    unexplored = graph.vertices[:]
    
    start = graph.edges[0]
    cheapestCost[start] = 0
    
    while unexplored != []:
        currentVertex = minCostV(cheapestCost, unexplored)
        unexplored.remove(currentVertex)
        explored.append(currentVertex)
        
        for edge in graph.getEdgesOf(currentVertex):
            neighbour = edge.start if edge.end == currentVertex else edge.end
            if neighbour in unexplored and edge.cost < cheapestCost[neighbour]:
                cheapestCost[neighbour] = edge.cost
                cheapestEdge[neighbour] = edge
    resultEdges = []
    for vertex in graph.vertices:
        if cheapestEdge[vertex] is not None:
            resultEdges.append(cheapestEdge[vertex])
    return resultEdges


def Euler107():
    raw = pathlib.Path('./resources/network.txt').read_text()
    
    lines = raw.split('\n')
    lines.remove('')
    matrix = []
    for line in lines:
        lineL = line.split(',')
        toAppend = []
        for l in lineL:
            try:
                toAppend.append(int(l))
            except ValueError:
                toAppend.append(-1)
        matrix.append(toAppend)
    graph = Graph(matrix)
    cheapestEdges = Prim(graph)
    return graph.getNetValue() - sum(v.cost for v in cheapestEdges)

start = time.time()
print(Euler107())
print(f'Took {time.time()-start}s')