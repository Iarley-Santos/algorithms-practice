#Encontra dois custos de sorvete que somam 'money' e retornar os indices desse sorvertes em ordem crescente.
# Obs: precisa ser dois sabores de sorvetes diferentes

def ice_cream_palor(money, arrey):
    for i in range(0, len(arrey)):
        #varre as opções acima da opção de i
        for j in range(i+1, len(arrey)):
            #verifica se o conjunto i com j é igual ao valor
            if arrey[i] + arrey[j] == money:
                result = [i + 1, j + 1]
                return result


#Utilizando HASH
def ice_cream_palor_hash(money, arrey):
    hash = {}
    for i in range(len(arrey)):
        complement = money - arrey[i]

        #verificar se o complemento ja existe no dicionario
        if complement in hash:
            return [hash[complement] + 1, i + 1]
        #se nao existir, deve ser adicionado no dicionario
        else:
            hash[arrey[i]] = i

money = 6
arrey = [3, 3]

print(ice_cream_palor_hash(money, arrey))