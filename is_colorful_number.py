def is_colorful_number(num):
    #passar num para string para facilitar manipular os termos
    s_num = str(num)
    list = {}

    for i in range(len(s_num)):
        product = 1 #para iniciar com um ao ir para o proximo termo
        #varrer todos os valores após o i
        for j in range(i, len(s_num)):
            product *= int(s_num[j])
            #verificar se ja possui esse valor na lista
            if product in list:
                return False
            else:
                list[product] = i
    return True

number = 10
result = is_colorful_number(number)
print(f"{number} is colerful number - {result}")