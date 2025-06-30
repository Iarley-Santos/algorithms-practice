def left_rotation(a, d):
    for i in range(0, d):
        element = a[0]
        a.pop(0)
        a.append(element)
    return a

a = [1, 2, 3, 4, 5]
d = 10

result = left_rotation(a, d)
print(f"A rotação a esquerda do vetor a é {result}")