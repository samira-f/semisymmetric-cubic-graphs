import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_automorphism(G, perm):
    n = G.number_of_nodes()
    mapping = {i: perm[i] for i in range(n)}

    for u, v in itertools.combinations(range(n), 2):
        if G.has_edge(u, v) != G.has_edge(mapping[u], mapping[v]):
            return False
    return True


def all_automorphisms(G):
    n = G.number_of_nodes()
    autos = []

    for perm in itertools.permutations(range(n)):
        if is_automorphism(G, perm):
            autos.append({i: perm[i] for i in range(n)})

    return autos


def is_vertex_transitive(G, autos):
    images = set()
    for auto in autos:
        images.add(auto[0])
    return len(images) == G.number_of_nodes()


def is_edge_transitive(G, autos):
    edges = list(G.edges())
    base_edge = edges[0]

    images = set()
    for auto in autos:
        u, v = base_edge
        mapped = tuple(sorted((auto[u], auto[v])))
        images.add(mapped)

    return len(images) == len(edges)


def main():
    G = nx.complete_bipartite_graph(3, 3)

    print("Cubic:", all(d == 3 for _, d in G.degree()))

    autos = all_automorphisms(G)
    print("Automorphisms:", len(autos))

    print("Vertex-transitive:", is_vertex_transitive(G, autos))
    print("Edge-transitive:", is_edge_transitive(G, autos))


if __name__ == "__main__":
    main()

def run_examples():
    graphs = {
        "K3,3": nx.complete_bipartite_graph(3, 3),
        "Cube Graph": nx.cubical_graph(),
        "Petersen Graph": nx.petersen_graph(),
    }

    for name, G in graphs.items():
        print("\n====================")
        print(f"Graph: {name}")
        print("====================")

        autos = all_automorphisms(G)

        print("Cubic:", all(d == 3 for _, d in G.degree()))
        print("Automorphisms:", len(autos))
        print("Vertex-transitive:", is_vertex_transitive(G, autos))
        print("Edge-transitive:", is_edge_transitive(G, autos))


if __name__ == "__main__":
    run_examples()

def draw_graph(G, title):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(title)
    plt.show()
