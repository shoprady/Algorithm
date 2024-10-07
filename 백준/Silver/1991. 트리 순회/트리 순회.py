class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
def preorder(r):
    print(r.data, end='')
    if r.left != '.':
        preorder(tree[r.left])
    if r.right != '.':
        preorder(tree[r.right])

def inorder(r):
    if r.left != '.':
        inorder(tree[r.left])
    print(r.data, end='')
    if r.right != '.':
        inorder(tree[r.right])

def postorder(r):
    if r.left != '.':
        postorder(tree[r.left])
    if r.right != '.':
        postorder(tree[r.right])
    print(r.data, end='')

if __name__ == "__main__":
    n = int(input())
    tree = {}
    for _ in range(n):
        root, left, right = input().split()
        tree[root] = Node(root, left, right)
    
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])