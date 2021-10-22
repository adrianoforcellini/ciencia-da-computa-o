# A estrutura deve estar ordenada para que a busca binária funcione
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start: end + 1])))
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return - 1


print(binary_search_iterative(data, 2))

# Observe como, a cada iteração, o algoritmo de busca binária corta o problema
# pela metade: primeiro ele corta a lista em dois e pega o elemento do meio.
# Depois ele vai para o lado onde o elemento que procura está e corta este lado
# novamente pela metade. Quando cortamos a entrada pela metade, a cada iteração,
# temos um padrão que segue a função matemática de logaritmo na base dois! 
# Assim, nosso algoritmo é O(log n) .
