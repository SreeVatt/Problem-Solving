from collections import deque
def bfs(graph,node):
    visited=[]
    queue=deque([node])
    while queue:
        current_node=queue.popleft()
        if current_node not in visited:
            print(current_node,end='=>')
            visited.append(current_node)
            queue.extend(graph[current_node]-set(visited))
    print("\b\b")



graph={
    'a': set(['b','c']),
    'b':set(['a','d','e','f']),
    'c':set(['f']),
    'd':set(['b']),
    'e':set(['b']),
    'f':set(['b'])
}
bfs(graph,'a')
