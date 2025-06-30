def a_very_big_sum(arrey):
    sum = 0
    for i in arrey:
        sum += i
    return sum

arrey = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(a_very_big_sum(arrey))