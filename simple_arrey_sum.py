'''
!/bin/python3

Complete the 'simpleArraySum' function below.

The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY ar as parameter.
'''

def simpleArraySum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum

if __name__ == '__main__':

    ar = (1, 2, 3, 4, 10, 11)

    result = simpleArraySum(ar)

    print(f"O resultado da soma do vetor {ar} é {result}")
