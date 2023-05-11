# NetworkX

## Graph
```
    import networkx as nx
    G = nx.Graph()
```

## Nodes
1. create a vertices
2. create edge from vertices
3. create graph from dict

### creating vertices
```
    G.add_node(1)
```
> adding vertices by vertices, without connections


### creating edges
 from 
```
    G.add_nodes_from([2, 3])
```
> new vertices are made from a non-ordered pair

### creating graph
```
    G.add_nodes_from([
        (4, {"color": "red"}),
        (5, {"color": "green"})
    ])
```
> you can make a new from a dict data structure
