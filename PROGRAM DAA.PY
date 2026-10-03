from collections import deque

# -------------------------------
# Social Network Graph
# -------------------------------

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["B", "C", "F"],
    "F": ["D", "E"]
}


# -------------------------------
# BFS - Minimum Hop Path
# -------------------------------

def bfs(graph, start, target):

    queue = deque([start])
    visited = set([start])

    # Store parent of each node
    parent = {start: None}

    visit_order = []

    while queue:

        current = queue.popleft()
        visit_order.append(current)

        # Target found
        if current == target:
            break

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)
                parent[neighbour] = current
                queue.append(neighbour)

    # Target not reachable
    if target not in parent:
        return [], visit_order

    # Construct path
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, visit_order


# -------------------------------
# DFS - Deep Graph Traversal
# -------------------------------

def dfs(graph, start, target):

    visited = set()
    visit_order = []
    parent = {start: None}

    def dfs_recursive(current):

        visited.add(current)
        visit_order.append(current)

        if current == target:
            return True

        for neighbour in graph[current]:

            if neighbour not in visited:

                parent[neighbour] = current

                if dfs_recursive(neighbour):
                    return True

        return False

    found = dfs_recursive(start)

    if not found:
        return [], visit_order

    # Construct path
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, visit_order


# -------------------------------
# Display Results
# -------------------------------

print("======================================")
print(" SOCIAL NETWORK CONNECTION FINDER")
print("======================================")

print("\nUsers in the Network:")

for user in graph:
    print(user, "->", graph[user])


source = input("\nEnter source user: ").upper()
target = input("Enter target user: ").upper()


# Check users
if source not in graph or target not in graph:

    print("\nInvalid user!")

else:

    # -------------------------------
    # BFS
    # -------------------------------

    bfs_path, bfs_order = bfs(graph, source, target)

    print("\n========== BFS RESULT ==========")

    print("BFS Visit Order:")
    print(" -> ".join(bfs_order))

    if bfs_path:

        print("\nShortest Connection Path:")
        print(" -> ".join(bfs_path))

        print("Degree of Connection:",
              len(bfs_path) - 1,
              "hops")

    else:

        print("No connection found.")


    # -------------------------------
    # DFS
    # -------------------------------

    dfs_path, dfs_order = dfs(graph, source, target)

    print("\n========== DFS RESULT ==========")

    print("DFS Visit Order:")
    print(" -> ".join(dfs_order))

    if dfs_path:

        print("\nDFS Connection Path:")
        print(" -> ".join(dfs_path))

    else:

        print("No connection found.")