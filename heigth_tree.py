class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        
        return root

    def height_tree(self, root):
        if root is None:
            return 0
        
        if root.right is not None:
            cont_r += self.height_tree(root.right)

        if root.left is not None:
            cont_l += self.height_tree(root.left)

        if cont_r >= cont_l:
            return cont_r
        else:
            return cont_l

if __name__ == '__main__':
    tree = Node(5)
    tree.insert(tree, 4)
    tree.insert(tree, 6)
    tree.insert(tree, 7)
    tree.insert(tree, 1)
    print(tree.right.data)
    print(tree.right.right.data)
    result=tree.height_tree(tree)
    print(result)
        