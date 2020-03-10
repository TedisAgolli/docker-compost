import sys
import yaml
import networkx as nx
import matplotlib.pyplot as plt


def createGraph(fPath):

    g = nx.DiGraph()
    with open(fPath) as f:
        compose = yaml.load(f, Loader=yaml.BaseLoader)
        allNodes = list(compose["services"].keys())
        for node in allNodes:
            g.add_node(node)
            for depends in compose["services"][node].get("depends_on", []):
                g.add_edge(node, depends)

    pos = nx.circular_layout(g)
    plt.figure(figsize=(20, 14))

    nodeAttr = [max(len(list(g.in_edges(n))) * 1500, 1000) for n in list(nx.nodes(g))]
    nx.draw_circular(
        g,
        node_size=nodeAttr,
        node_color="lightblue",
        linewidths=0.25,
        font_size=10,
        font_weight="bold",
        with_labels=True,
        dpi=1000,
        scale=2,
    )
    plt.show()
    plt.savefig("compost.png")


if __name__ == "__main__":
    try:
        fPath = sys.argv[1]
    except IndexError:
        print("Please path the compose file path")
        exit()

    createGraph(fPath)

