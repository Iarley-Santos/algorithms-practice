#
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, root, data):
        #caso base
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data >= root.data:
            root.right = self.insert(root.right, data)
        
        return root

if __name__ == '__main__':

    # 1. Criar a RAÍZ da sua árvore com o PRIMEIRO valor
    # Vamos fazer o 4 ser o nó raiz.
    root_node = Node(4)

    root_node.right = Node(5)
    root_node.right = Node(6)

    root_node.insert(root_node, 2)

    print(root_node.left.data)