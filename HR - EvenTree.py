# https://www.hackerrank.com/challenges/even-tree/problem?isFullScreen=true
# rekurzio, graf


adj_m = {}
visited = []
subtree_sizes = []


def add_to_adj_m(a, b, adj_matrix):
    if a in adj_matrix:
        if b not in adj_matrix[a]:
            adj_matrix[a].append(b)
    else:
        adj_matrix[a] = [b]


def get_subtree_size(node):
    global adj_m
    global visited

    visited[node] = True

    subtree_size = 1

    for child in adj_m[node]:
        if visited[child] == False:
            subtree_size += get_subtree_size(child)

    subtree_sizes[node] = subtree_size
    return subtree_size


def evenForest(t_nodes, t_edges, t_from, t_to):
    global adj_m
    global visited
    global subtree_sizes

    visited = [False] * (t_nodes + 1)
    visited[0] = True

    subtree_sizes = [0] * (t_nodes + 1)

    for i in range(t_edges):
        add_to_adj_m(t_from[i], t_to[i], adj_m)
        add_to_adj_m(t_to[i], t_from[i], adj_m)
    ######

    get_subtree_size(1)

    vagva = 0
    for i in range(2, t_nodes + 1):
        if subtree_sizes[i] % 2 == 0:
            vagva += 1
    return vagva