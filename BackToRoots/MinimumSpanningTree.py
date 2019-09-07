class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
    
    def getVertices(self):
        return list(self.__graph_dict.keys())
    
    def getEdges(self):
        edges = []
        for vertex in self.__graph_dict:
            for entry in self.__graph_dict[vertex]:
                arb = [vertex]+entry
                if(set(arb) not in edges):
                    edges.append(set(arb))
        return edges
    
    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def addEdge(self,edge,weight):
        # Tuples are immutable
        (vertex1, vertex2) = tuple(set(edge))
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1] += [vertex2, weight]
        else:
            self.__graph_dict[vertex1] = [vertex2, weight]
            
    def printer(self):
        print(self.__graph_dict)
        
g = {
    "a": [["b",8], ["g",11], ["i",4]],
    "b": [["c",7], ["e",4], ["h",2], ["a",8]],
    "c": [["b",7], ["e",14], ["d",9]],
    "d": [["c",9], ["e",10]],
    "e": [["d",10], ["c",14], ["b",4], ["f",2]],
    "f": [["g",1], ["h",6], ["e",2]],
    "g": [["h",7], ["a",11], ["i",8],["f",1]],
    "h": [["b",2], ["g",7], ["f",6]],
    "i": [["g",8], ["a",4]]
}
graph = Graph(g)
# graph.addEdge({"a","b"},8)
# graph.addEdge({"a","g"},11)
# graph.addEdge({"b","c"},7)
# graph.printer()
print(graph.getVertices())
print(graph.getEdges())

