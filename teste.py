class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    #para adicionar um novo no no final da lista
    def append(self, data):
        new_node = Node(data)

        #se for o primeiro da lista 
        if self.head == None:
            self.head = new_node
            return
        
        #se nao for o primeiro da lista
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    #para adicionar um novo no em uma posição especifica
    def insert_node(self, data, position):
        new_node = Node(data)

        #caso seja na primeira posição
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        #se nao tiver na primeira posição é precios percorrer a lista ate chegar no no da posição anterior
        current = self.head
        cont = 0
        while (cont < position -1) and (current.next != None):
            current = current.next
            cont+=1
        #apontar o new node para o no que o anterior a ele estava apontando
        new_node.next = current.next
        #apontar o no anterior para o novo no adicionado
        current.next = new_node


    def print_list(self):
        current_node = self.head
        elements = []

        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        
        print("->".join(elements))

minha_lista = LinkedList()
minha_lista.append(10)
minha_lista.append(20)
minha_lista.append(30)
minha_lista.insert_node(25, 2)
minha_lista.print_list()
        