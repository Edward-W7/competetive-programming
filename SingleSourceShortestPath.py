inpt = [int(i) for i in input().split()]
n = inpt[0]
m = inpt[1]
graph = []
for i in range(n):
   graph.append([90000000]*n)

dist = [90000000] * n
visited = [0] * n

for i in range(len(graph)):
    graph[i][i] = 0
for i in range(m):
    inpt = [int(i) for i in input().split()]
    if inpt[2] < graph[inpt[0]-1][inpt[1]-1]:
        graph[inpt[0]-1][inpt[1]-1] = inpt[2]
        graph[inpt[1]-1][inpt[0]-1] = inpt[2]
for i in range(n):
    if graph[0][i] != 90000000:
        dist[i] = graph[0][i]
visited[0] = 1
while 0 in visited:
    currd = 9000000000
    for i in range(n):
        if visited[i] == 0 and dist[i] < currd:
            u = i
            currd = dist[i]
    visited[u] = 1
    for v in range(len(graph[u])):
        alt = dist[u] + graph[u][v]
        if alt < dist[v]:
            dist[v] = alt
for i in dist:
    if i >= 90000000:
        print(-1)
    else:
        print(i)

