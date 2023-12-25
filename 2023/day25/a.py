import networkx as nx
import matplotlib.pyplot as plt

input = open("input.txt").read().split('\n')

graph = {}

G = nx.Graph()

for l in input:
    k, v = l.split(":")
    vals = list(v.strip().split(" "))
    graph[k] = vals
    for val in vals:
        G.add_edge(k, val, capacity=1)

print(graph)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()  

# after drawing the graph I can see where to cut
cut_points = [("ptj", "qmr"), ("lsv", "lxt"), ("dhn", "xvh")]

cut_num = 0
for c in cut_points:
    num, (L,R) = nx.minimum_cut(G, c[0], c[1])
    cut_num += 1
    if cut_num == 2:
        print(L, R)
        print(len(L) * len(R))

# theres no part b for christmas :)