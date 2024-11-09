import sys
sys.setrecursionlimit(int(2e4))

class TreeNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None ###
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.item)
        
tree = []
while True:
    try:
        tree.append(int(input()))
    except: break
        
root = TreeNode(tree[0])
root.parent = None
curr = root

for i in range(1, len(tree)):
    node = TreeNode(tree[i])
    if tree[i] < curr.item:
        curr.left = node
        node.parent = curr
        curr = node
    else: # tree[i] >= curr.item
        while curr != root:
            if tree[i] > curr.parent.item:
                curr = curr.parent
            else: break
        while curr.right:
            curr = curr.right
        curr.right = node
        node.parent = curr
        curr = node
        
postorder(root)