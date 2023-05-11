import matplotlib.pyplot as plt 
import networkx as nx

G = nx.Graph()
print('VERTICES')   #---------------------
question = "Insira o número de vértices: "
n = int(input(question))

for i in range(n):
    G.add_node(i)
    i = i + 1

# print(G)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()