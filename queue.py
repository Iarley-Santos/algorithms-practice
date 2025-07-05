#criando uma fila utilizando apenas duas pilhas
class Queue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def enqueue(self, data):
        #apenas adicione o dado na pilha de entrada
        self.input_stack.append(data)

    def dequeue(self):
        #verifica se a pilha de saida nao esta vazia
        if not self.output_stack:
            #equanto tiver valor na pilha de entrada pegue o valor do topo e armazene na pilha da saida
            while self.input_stack:
                top_stack = self.input_stack.pop()
                self.output_stack.append(top_stack)
        return self.output_stack.pop()
            
    def peek(self):
        #verifica se a pilha de saida nao esta vazia
        if not self.output_stack:
            #equanto tiver valor na pilha de entrada pegue o valor do topo e armazene na pilha da saida
            while self.input_stack:
                top_stack = self.input_stack.pop()
                self.output_stack.append(top_stack)
        return self.output_stack[-1]
        
#teste
fila = Queue()
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
print(fila.peek())
print(fila.dequeue())
print(fila.dequeue())
print(fila.dequeue())
fila.enqueue(40)
print(fila.dequeue())