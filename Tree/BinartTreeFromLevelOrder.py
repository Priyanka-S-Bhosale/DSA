from collections import deque

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    
def binaryFromLevelOrder(data):
    count = 0
    q = deque()
    root = TreeNode(data[0])
    q.append(root)
    curr = TreeNode(None)
    for i in range(1, len(data)):
        node = TreeNode(data[i])
        if count == 0:
            curr = q.popleft()
        if count == 0:
            count += 1
            curr.left = node
        else:
            count = 0
            curr.right = node
        if data[i] != '#':
            q.append(node)
    return root

data = [1, 2, 3, '#', '#', 4, '#', '#', 5]
root = binaryFromLevelOrder(data)
print(root.val)  # Print the value of the root node
preorder(root)
