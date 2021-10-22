# Complexidade de tempo e de espaço

def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
            array_of_squares.append(number * number)

    return array_of_squares

# Para o algoritmo acima, aumentar a entrada em dez vezes aumenta em dez 
# vezes o tempo de execução! A sua ordem de complexidade, portanto, é O(n) .
# Na maior parte das vezes em que falarmos de Ordem de Complexidade, estamos 
# falando disso: do tempo que o algoritmo vai demorar para executar, ou 
# complexidade de tempo . Há também uma outra complexidade: a complexidade de 
# espaço , se referindo ao espaço em memória que o algoritmo ocupa.

# A ideia é a mesma:  na medida em que a entrada aumenta, quanto o espaço em
# memória usado pelo algoritmo aumenta? No exemplo acima, o algoritmo povoa e 
# retorna um array de tamanho n , sendo n o tamanho do array entrado, e o 
# retorna. Assim sendo, sua complexidade de espaço é O(n) !


# Ex
# Exercício 1: Qual a Ordem de Complexidade (complexidade de tempo)
# do algoritmo abaixo? E a complexidade de espaço?
def multiply_array(numbers):
    result = 0
    for number in numbers:
            result *= number

    return result

# resposta  O(1)
