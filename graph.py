import sys
from graphviz import Digraph
import yaml


if __name__ == "__main__":
    try:
        fPath = sys.argv[1]
    except IndexError:
        print("Please path the compose file path")
        exit()

    g = Digraph("G", filename="compose.gv", engine="sfdp")
    with open(fPath) as f:
        compose = yaml.load(f, Loader=yaml.BaseLoader)
        allNodes = list(compose["services"].keys())
        for node in allNodes:
            g.node(node)
            for depends in compose["services"][node].get("depends_on", []):
                g.edge(node, depends)
    g.view()
