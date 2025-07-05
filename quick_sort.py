#Implementa o algoritmo de ordenação Quick Sort (Ordenação Rápida)
#utilizando o paradigma "dividir e conquistar".
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivo = arr[0]
    left = []
    right = []
    equal = []
    equal.append(pivo)
    
    for i in range(1, len(arr)):
        if arr[i] > pivo:
            right.append(arr[i])
        elif arr[i] < pivo:
            left.append(arr[i])
        else:
            equal.append(arr[i])
    
    l = quick_sort(left)
    r = quick_sort(right)

    result = l + equal + r
    print(*result)
    return result

if __name__ == '__main__':
    arr = [5, 8, 1, 3, 7, 9, 2]
    quick_sort(arr)
