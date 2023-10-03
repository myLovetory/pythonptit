from collections import deque

# Function to check if a point is within the bounds of the arena
def is_valid(x, y):
    return 0 <= x <= 109 and 0 <= y <= 109

# Function to build the graph from the given barriers
def build_graph(barriers):
    graph = {}
    for x, y1, y2 in barriers:
        for y in range(y1, y2 + 1):
            if (x, y) not in graph:
                graph[(x, y)] = set()
            if is_valid(x - 1, y - 1):
                graph[(x, y)].add((x - 1, y - 1))
            if is_valid(x - 1, y):
                graph[(x, y)].add((x - 1, y))
            if is_valid(x - 1, y + 1):
                graph[(x, y)].add((x - 1, y + 1))
            if is_valid(x, y - 1):
                graph[(x, y)].add((x, y - 1))
            if is_valid(x, y + 1):
                graph[(x, y)].add((x, y + 1))
            if is_valid(x + 1, y - 1):
                graph[(x, y)].add((x + 1, y - 1))
            if is_valid(x + 1, y):
                graph[(x, y)].add((x + 1, y))
            if is_valid(x + 1, y + 1):
                graph[(x, y)].add((x + 1, y + 1))
    return graph

# Function to find the shortest path from A to B using BFS
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1

# Read input
T = int(input())
for _ in range(T):
    xA, yA, xB, yB = map(int, input().split())
    N = int(input())
    barriers = []
    for _ in range(N):
        x, y1, y2 = map(int, input().split())
        barriers.append((x, y1, y2))

    # Build the graph
    graph = build_graph(barriers)

    # Find the shortest path from A to B
    steps = shortest_path(graph, (xA, yA), (xB, yB))

    # Print the result
    print(steps)