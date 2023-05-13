def read_graph(file_name):
    with open(file_name, 'r') as f:
        n, m = map(int, f.readline().split())
        edges = [tuple(map(int, line.split())) for line in f]
    return n, m, edges


def get_degree_sequence(n, edges):
    degrees = [0] * n
    for u, v in edges:
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    return degrees


def get_order(n):
    return n


def get_size(m):
    return m


def get_vertex_degrees(n, edges):
    degrees = get_degree_sequence(n, edges)
    return {i + 1: degree for i, degree in enumerate(degrees)}


def get_graph_degree_sequence(n, edges):
    return tuple(get_degree_sequence(n, edges))


if __name__ == '__main__':
    n, m, edges = read_graph('graf.txt')
    print('Order:', get_order(n))
    print('Size:', get_size(m))
    print('Vertex degrees:', get_vertex_degrees(n, edges))
    print('Degree sequence:', get_graph_degree_sequence(n, edges))
