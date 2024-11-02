def delete_nodes(nodes, d):
    nodes[d] = -2
    for i in range(len(nodes)):
        if nodes[i] == d:
            delete_nodes(nodes, i)

n = int(input())
nodes = list(map(int, input().split()))
d = int(input())

# remove node
delete_nodes(nodes, d)

# count leaf nodes
leaf = 0
for i in range(len(nodes)):
    if i not in nodes and nodes[i] != -2:
        leaf += 1
print(leaf)