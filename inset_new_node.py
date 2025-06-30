class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    #para adicionar um novo nó no final da lista
    def append(self, data):
        new_node = Node(data)

        #se a lista estiver vazia, o novo no se torna a cabeça
        if self.head == None:
            self.head = new_node
            return
        
        #se a lista nao estiver vazia, precisamos encontrar o ultimo nó
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        #agora o ultimo no aponta para o novo no
        last_node.next = new_node
    
    def insert_new_node_at_position(self, data, position):
        new_node = Node(data)

        #caso a posição seja a inicial
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        cont = 0

        #enquanto o nao chegar no anterior a posição e nao ultrapassar a lista tambem
        while (cont < position - 1) and (current.next != None):
            current =  current.next
            cont += 1
        
        #aponta para o proximo no para dar continuidade a lista
        new_node.next = current.next

        #aponta para o novo no para
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
minha_lista.insert_new_node_at_position(25,2)
minha_lista.insert_new_node_at_position(28,3)
minha_lista.insert_new_node_at_position(5,0)
minha_lista.print_list()