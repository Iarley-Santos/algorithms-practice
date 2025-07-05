#Verifica se uma string de parênteses, colchetes e chaves está balanceada.
def is_balanced(s):
    map_char = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    open = ['(', '[', '{']

    stack = []

    for i in range(len(s)):
        #verifica se é um caractere de abertura, se for, adicione na pilha
        if s[i] in open:
            stack.append(s[i])
        #se nao for, pegue o ultimo da pilha
        else:
            top_list = stack.pop()
            print(top_list)
            #verifica se o ultimo da pilha possui o seu equivalente no mapa
            if top_list != map_char[s[i]]:
                return 'NO'

    #verifica se a pilha esta vazia
    if not stack:
        return 'YES'
    else:
        return 'NO'

input = "{{[()]}}"
output = is_balanced(input)
print(f"{input} -> {output}")
