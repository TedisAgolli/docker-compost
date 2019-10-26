from graphviz import Graph
import yaml

g = Graph('G',filename='compose.gv',engine='sfdp')
with open('docker-compose.yml') as f:
    compose = yaml.load(f,Loader=yaml.BaseLoader)
    allNodes = list(compose['services'].keys())
    for node in allNodes:
        g.node(node)
        for depends in compose['services'][node].get('depends_on',[]):
            g.edge(node,depends)
g.view()