import sys
from heapq import heappop, heappush
input_string = input()
user_list = input_string.split()
user_list = [int(i) for i in user_list]
N = user_list[0]
M = user_list[1]
graphlst = []


for i in range(M):
    input_strng = input()
    lst = input_strng.split()
    lst = [int(i) for i in lst]
    graphlst.append(lst)

for i in range(len(graphlst)):
        for y in range(3):
            if y != 2:
                graphlst[i][y] -= 1
class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
class Graph:
    def __init__(self, side, n):
        self.adjList = [[] for _ in range(n)]
        for (source, dest, weight) in side:
            self.adjList[source].append((dest, weight))
def findroute(prev, i, route):
    if i >= 0:
        findroute(prev, prev[i], route)
        route.append(i)
def shortestpathalg(graph, source, n):
    pq = []
    heappush(pq, Node(source))
    dist = [sys.maxsize] * n
    dist[source] = 0
    done = [False] * n
    done[source] = True
    prev = [-1] * n
    while pq:
        node = heappop(pq)
        u = node.vertex
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
        done[u] = True
    route = []
    for i in range(n):

        findroute(prev, i, route)
        if dist[i] == sys.maxsize:
            print(-1)
        else:
            print(dist[i])
        route.clear()

shortestpathalg(Graph(graphlst, N), 0, N)
