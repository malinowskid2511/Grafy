def is_simple_graph(adj_list):
    """
    :param
    :return:
    """
    for u in adj_list:
        for v in adj_list[u]:
            if u == v or v in adj_list[u]:
                return False
    return True

# Load graph from file
with open('graf.txt', 'r') as f:
    num_vertices, num_edges = map(int, f.readline().split())
    adj_list = {v: [] for v in range(1, num_vertices + 1)}
    for _ in range(num_edges):
        u, v = map(int, f.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

# Check if the graph is simple or general
if is_simple_graph(adj_list):
    print('Graf jest grafem prostym.')
else:
    print('Graf jest grafem ogólnym.')