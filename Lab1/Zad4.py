# Funkcja do obliczania dopełnienia grafu
def complement(adj_list, num_vertices):
    # Inicjalizacja listy sąsiedztwa dla grafu dopełnienia
    comp_adj_list = {v: [] for v in range(1, num_vertices + 1)}
    # Przejście po wszystkich parach wierzchołków
    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            # Jeśli wierzchołki nie są połączone krawędzią w grafie oryginalnym, to łączymy je krawędzią w grafie dopełnienia
            if u != v and v not in adj_list[u]:
                comp_adj_list[u].append(v)
    # Zwracamy listę sąsiedztwa dla grafu dopełnienia
    return comp_adj_list

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

# Sprawdzamy, czy graf jest grafem pełnym
is_complete = True
for u in adj_list:
    for v in adj_list:
        # Jeśli istnieją dwa różne wierzchołki, które nie są połączone krawędzią, to graf nie jest pełny
        if u != v and v not in adj_list[u]:
            is_complete = False
            break
    if not is_complete:
        break

# Jeśli graf nie jest pełny, to obliczamy jego dopełnienie i wypisujemy krawędzie
if not is_complete:
    print("Graf nie jest grafem pełnym.")
    comp_adj_list = complement(adj_list, num_vertices)
    print("Krawędzie grafu dopełnienia:")
    for u in comp_adj_list:
        for v in comp_adj_list[u]:
            print(f"{u} {v}")
else:
    print("Graf jest grafem pełnym.")
