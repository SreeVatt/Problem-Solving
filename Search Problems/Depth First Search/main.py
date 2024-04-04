def dfs(graph,node,visited):
    
    if node not in visited:
        print(node,end='=>')
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)
            
    
            
visited=[]
graph={
    'a': set(['b','c']),
    'b':set(['a','d','e','f']),
    'c':set(['a','f']),
    'd':set(['b']),
    'e':set(['b']),
    'f':set(['b'])
}
dfs(graph,'a',visited)
print('\b\b')
