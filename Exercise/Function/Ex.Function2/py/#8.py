
#* 8. Check for Cycle in a Graph

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

# Input the graph
n = int(input("Enter number of nodes: "))
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
print("Cycle exists in the graph." if cycle_exists else "No cycle in the graph.")


#? ตัวอย่างการ input
#* Enter number of nodes: 3
#* Enter the edges for node (space-separated): 1 2
#* Enter the edges for node (space-separated): 2 3
#* Enter the edges for node (space-separated): 3 1
