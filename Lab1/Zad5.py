# Wczytujemy opis grafu z pliku
with open('graf.txt', 'r') as f:
    # Wczytujemy liczbę wierzchołków i krawędzi
    num_vertices, num_edges = map(int, f.readline().split())
    # Inicjalizujemy listę sąsiedztwa
    adj_list = {v: [] for v in range(1, num_vertices + 1)}
    # Wczytujemy krawędzie
    for _ in range(num_edges):
        u, v = map(int, f.readline().split())
        # Dodajemy krawędzie do listy sąsiedztwa w obu kierunkach
        adj_list[u].append(v)
        adj_list[v].append(u)

# Wyświetlamy listę sąsiedztwa na ekranie
for u in adj_list:
    print(f"Wierzchołek {u}: {adj_list[u]}")