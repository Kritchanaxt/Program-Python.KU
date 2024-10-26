

#? Ex.Function2 - #8

def has_cycle(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
        
    rec_stack[node] = False
    return False

n = int(input("Enter number of node: "))
graph = {}

for _ in range(n):
    edges = list(map(int, input("Enter the edges for node (space-separated): ").split()))
    node = edges[0]
    if node not in graph:
        graph[node] = []
    for neighbor in edges[1:]:
        if neighbor not in graph:
            graph[neighbor] = []
        graph[node].append(neighbor)

visited = {node: False for node in graph}
rec_stack = {node: False for node in graph}

cycle_exists = any(has_cycle(graph, node, visited, rec_stack) for node in graph if not visited[node])
print("Cycle exits in the graph." if cycle_exists else "No cycle in the graph.")