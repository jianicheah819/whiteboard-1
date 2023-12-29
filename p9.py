#use DFS (Depth First Tarversal) technique 
from collections import defaultdict


class Graph():
    def __init__(self, vertices): #vertices is the total number of node
        self.graph = defaultdict(list) #to store each path from start node to end node
        self.V = vertices

    def addEdge(self, u, v): #u and v represent the start and end node
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True #to check if the node will be pass by
        recStack[v] = True #track node in the current recursion stack

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

    def findPath(self, start, end, path):
        path.append(start)

        if start == end:
            return True

        visited = set(path)  # Keep track of visited nodes to avoid cycles

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                if self.findPath(neighbour, end, path):
                    return True

        path.pop()
        return False


# Driver code
if __name__ == '__main__':
    g = Graph(8)
    g.addEdge('A', 'B')
    g.addEdge('B', 'A')
    g.addEdge('B', 'D')
    g.addEdge('B', 'C')
    g.addEdge('B', 'F')
    g.addEdge('B', 'E')
    g.addEdge('C', 'F')
    g.addEdge('F', 'G')
    g.addEdge('D', 'E')
    g.addEdge('E', 'F')
    g.addEdge('D', 'G')

    start_node = 'A'
    end_node = 'G'

    if g.isCyclic():
        print("Graph contains cycle")
    else:
        path = []
        if g.findPath(start_node, end_node, path):
            print(f"Path from {start_node} to {end_node}: {path}")
        else:
            print(f"No path from {start_node} to {end_node}")

#Use Graph class and import the library defaultdict from collections