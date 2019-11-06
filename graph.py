import sys
import yaml
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":
    try:
        fPath = sys.argv[1]
    except IndexError:
        print("Please path the compose file path")
        exit()

    g = nx.DiGraph()
    with open(fPath) as f:
        compose = yaml.load(f, Loader=yaml.BaseLoader)
        allNodes = list(compose["services"].keys())
        for node in allNodes:
            g.add_node(node)
            for depends in compose["services"][node].get("depends_on", []):
                g.add_edge(node, depends)

    pos = nx.circular_layout(g)

    for node, coords in pos.items():
        x, y = coords
        shift = lambda val: 0.1 if val > 0 else -0.1
        plt.text(x + shift(x), y + shift(y), node)

    nx.draw_circular(g)
    # plt.show()
    plt.savefig("compost.png")
