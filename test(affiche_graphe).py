import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
# G=nx.Graph()
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_edge("A","B")
# G.add_edge("B","C")
# G.add_edge("C","A")
 
# print("Nodes: " + str(G.nodes()))
# print("Edges: " + str(G.edges()))

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

nx.draw(G)
plt.show() # display


