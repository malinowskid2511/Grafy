def read_graph(file_name):
    with open(file_name, 'r') as f:
        n, m = map(int, f.readline().split())
        edges = [tuple(map(int, line.split())) for line in f]
    return n, m, edges


def get_vertices(n):
    return set(range(1, n + 1))


def get_edges(edges):
    return set(edges)


def get_adjacency_matrix(n, edges):
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj_matrix[u - 1][v - 1] = 1
        adj_matrix[v - 1][u - 1] = 1
    return adj_matrix


def get_incidence_matrix(n, m, edges):
    inc_matrix = [[0] * m for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        inc_matrix[u - 1][i] = 1
        inc_matrix[v - 1][i] = 1
    return inc_matrix


if __name__ == '__main__':
    n, m, edges = read_graph('graf.txt')
    print('Number of vertices:', n)
    print('Vertices:', get_vertices(n))
    print('Number of edges:', m)
    print('Edges:', get_edges(edges))
    print('Adjacency matrix:')
    for row in get_adjacency_matrix(n, edges):
        print(row)
    print('Incidence matrix:')
    for row in get_incidence_matrix(n, m, edges):
        print(row)
